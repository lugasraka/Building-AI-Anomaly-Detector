"""
Monitoring and Drift Detection for GreenLens AI
Tracks model performance, data drift, and system health
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from scipy import stats
import json
import os


class DriftDetector:
    """Detects data drift and model performance degradation"""
    
    def __init__(self, reference_stats_path: str = "logs/reference_stats.json"):
        self.reference_stats_path = reference_stats_path
        self.drift_threshold = 0.1  # PSI threshold
        self.ks_threshold = 0.05    # KS test p-value threshold
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Create necessary directories"""
        os.makedirs(os.path.dirname(self.reference_stats_path), exist_ok=True)
    
    def calculate_reference_stats(self, df: pd.DataFrame, features: List[str]) -> Dict:
        """
        Calculate reference statistics from training data
        
        Args:
            df: Training dataframe
            features: List of feature columns to track
        
        Returns:
            Dictionary of reference statistics
        """
        stats_dict = {
            "calculated_at": datetime.now().isoformat(),
            "n_samples": len(df),
            "features": {}
        }
        
        for feature in features:
            if feature in df.columns:
                feature_stats = {
                    "mean": float(df[feature].mean()),
                    "std": float(df[feature].std()),
                    "min": float(df[feature].min()),
                    "max": float(df[feature].max()),
                    "median": float(df[feature].median()),
                    "percentile_25": float(df[feature].quantile(0.25)),
                    "percentile_75": float(df[feature].quantile(0.75)),
                    "histogram": self._calculate_histogram(df[feature])
                }
                stats_dict["features"][feature] = feature_stats
        
        # Save reference stats
        with open(self.reference_stats_path, 'w') as f:
            json.dump(stats_dict, f, indent=2)
        
        return stats_dict
    
    def _calculate_histogram(self, series: pd.Series, bins: int = 10) -> List:
        """Calculate histogram bins for a series"""
        hist, bin_edges = np.histogram(series.dropna(), bins=bins)
        return {
            "counts": hist.tolist(),
            "bin_edges": bin_edges.tolist()
        }
    
    def load_reference_stats(self) -> Optional[Dict]:
        """Load reference statistics from file"""
        if os.path.exists(self.reference_stats_path):
            with open(self.reference_stats_path, 'r') as f:
                return json.load(f)
        return None
    
    def detect_drift(self, current_df: pd.DataFrame, features: List[str]) -> Dict:
        """
        Detect drift between current data and reference data
        
        Args:
            current_df: Current dataframe
            features: List of feature columns to check
        
        Returns:
            Dictionary with drift metrics and alerts
        """
        reference_stats = self.load_reference_stats()
        if not reference_stats:
            return {"error": "No reference stats available. Train model first."}
        
        drift_results = {
            "checked_at": datetime.now().isoformat(),
            "n_current_samples": len(current_df),
            "features": {},
            "overall_drift_score": 0.0,
            "drift_detected": False,
            "alerts": []
        }
        
        total_drift_score = 0
        drift_count = 0
        
        for feature in features:
            if feature not in current_df.columns or feature not in reference_stats["features"]:
                continue
            
            ref_stats = reference_stats["features"][feature]
            current_series = current_df[feature].dropna()
            
            # Calculate PSI (Population Stability Index)
            psi_score = self._calculate_psi(
                ref_stats["histogram"], 
                current_series
            )
            
            # Perform KS test
            # Reconstruct reference distribution from stats (approximate)
            ref_mean = ref_stats["mean"]
            ref_std = ref_stats["std"]
            ref_samples = np.random.normal(ref_mean, ref_std, 1000)
            
            ks_statistic, ks_pvalue = stats.ks_2samp(ref_samples, current_series)
            
            # Determine if drift detected
            drift_detected = psi_score > self.drift_threshold or ks_pvalue < self.ks_threshold
            
            feature_result = {
                "psi_score": float(psi_score),
                "ks_statistic": float(ks_statistic),
                "ks_pvalue": float(ks_pvalue),
                "drift_detected": drift_detected,
                "current_mean": float(current_series.mean()),
                "current_std": float(current_series.std()),
                "reference_mean": ref_stats["mean"],
                "mean_shift_pct": float((current_series.mean() - ref_stats["mean"]) / ref_stats["mean"] * 100) if ref_stats["mean"] != 0 else 0
            }
            
            drift_results["features"][feature] = feature_result
            total_drift_score += psi_score
            
            if drift_detected:
                drift_count += 1
                drift_results["alerts"].append(
                    f"Drift detected in {feature}: PSI={psi_score:.3f}, p-value={ks_pvalue:.3f}"
                )
        
        # Calculate overall drift
        n_features = len([f for f in features if f in current_df.columns])
        drift_results["overall_drift_score"] = total_drift_score / n_features if n_features > 0 else 0
        drift_results["drift_detected"] = drift_count > 0
        drift_results["drift_feature_count"] = drift_count
        drift_results["total_features_checked"] = n_features
        
        return drift_results
    
    def _calculate_psi(self, reference_histogram: Dict, current_series: pd.Series, bins: int = 10) -> float:
        """
        Calculate Population Stability Index (PSI)
        
        PSI < 0.1: No significant change
        0.1 <= PSI < 0.25: Moderate change
        PSI >= 0.25: Significant change
        """
        # Calculate current histogram using same bins
        bin_edges = reference_histogram["bin_edges"]
        current_hist, _ = np.histogram(current_series, bins=bin_edges)
        
        # Get reference counts
        ref_counts = np.array(reference_histogram["counts"])
        
        # Calculate percentages
        ref_pct = ref_counts / ref_counts.sum()
        current_pct = current_hist / current_hist.sum() if current_hist.sum() > 0 else np.zeros_like(current_hist)
        
        # Calculate PSI
        psi = 0
        for i in range(len(ref_pct)):
            if ref_pct[i] > 0 and current_pct[i] > 0:
                psi += (current_pct[i] - ref_pct[i]) * np.log(current_pct[i] / ref_pct[i])
        
        return float(psi)


class PerformanceTracker:
    """Tracks model performance metrics over time"""
    
    def __init__(self, log_path: str = "logs/performance_log.json"):
        self.log_path = log_path
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Create necessary directories"""
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
    
    def log_prediction(
        self,
        model_id: str,
        timestamp: datetime,
        latency_ms: float,
        anomaly_detected: bool,
        anomaly_score: float,
        input_features: Dict
    ):
        """Log a single prediction event"""
        log_entry = {
            "model_id": model_id,
            "timestamp": timestamp.isoformat(),
            "latency_ms": latency_ms,
            "anomaly_detected": anomaly_detected,
            "anomaly_score": float(anomaly_score),
            "input_features": {k: float(v) for k, v in input_features.items()}
        }
        
        # Append to log file
        logs = []
        if os.path.exists(self.log_path):
            with open(self.log_path, 'r') as f:
                logs = json.load(f)
        
        logs.append(log_entry)
        
        # Keep only last 10000 entries to manage file size
        if len(logs) > 10000:
            logs = logs[-10000:]
        
        with open(self.log_path, 'w') as f:
            json.dump(logs, f, indent=2)
    
    def get_performance_summary(self, hours: int = 24) -> Dict:
        """Get performance summary for the last N hours"""
        if not os.path.exists(self.log_path):
            return {"error": "No performance logs available"}
        
        with open(self.log_path, 'r') as f:
            logs = json.load(f)
        
        cutoff_time = datetime.now() - timedelta(hours=hours)
        recent_logs = [
            log for log in logs 
            if datetime.fromisoformat(log["timestamp"]) > cutoff_time
        ]
        
        if not recent_logs:
            return {
                "period_hours": hours,
                "total_predictions": 0,
                "message": "No predictions in the specified time period"
            }
        
        latencies = [log["latency_ms"] for log in recent_logs]
        anomaly_count = sum(1 for log in recent_logs if log["anomaly_detected"])
        
        return {
            "period_hours": hours,
            "total_predictions": len(recent_logs),
            "anomaly_count": anomaly_count,
            "anomaly_rate": anomaly_count / len(recent_logs) * 100,
            "latency_stats": {
                "mean_ms": np.mean(latencies),
                "median_ms": np.median(latencies),
                "min_ms": min(latencies),
                "max_ms": max(latencies),
                "p95_ms": np.percentile(latencies, 95),
                "p99_ms": np.percentile(latencies, 99)
            },
            "anomaly_score_stats": {
                "mean": np.mean([log["anomaly_score"] for log in recent_logs]),
                "max": max([log["anomaly_score"] for log in recent_logs]),
                "min": min([log["anomaly_score"] for log in recent_logs])
            }
        }
    
    def get_prediction_trend(self, hours: int = 24, interval_minutes: int = 60) -> List[Dict]:
        """Get prediction trends over time intervals"""
        if not os.path.exists(self.log_path):
            return []
        
        with open(self.log_path, 'r') as f:
            logs = json.load(f)
        
        cutoff_time = datetime.now() - timedelta(hours=hours)
        recent_logs = [
            log for log in logs 
            if datetime.fromisoformat(log["timestamp"]) > cutoff_time
        ]
        
        # Group by time intervals
        trends = []
        current_time = cutoff_time
        end_time = datetime.now()
        
        while current_time < end_time:
            interval_end = current_time + timedelta(minutes=interval_minutes)
            interval_logs = [
                log for log in recent_logs
                if current_time <= datetime.fromisoformat(log["timestamp"]) < interval_end
            ]
            
            if interval_logs:
                trends.append({
                    "interval_start": current_time.isoformat(),
                    "interval_end": interval_end.isoformat(),
                    "prediction_count": len(interval_logs),
                    "anomaly_count": sum(1 for log in interval_logs if log["anomaly_detected"]),
                    "avg_latency_ms": np.mean([log["latency_ms"] for log in interval_logs]),
                    "avg_anomaly_score": np.mean([log["anomaly_score"] for log in interval_logs])
                })
            
            current_time = interval_end
        
        return trends


class MonitoringDashboard:
    """Main monitoring interface combining drift detection and performance tracking"""
    
    def __init__(self):
        self.drift_detector = DriftDetector()
        self.performance_tracker = PerformanceTracker()
    
    def get_health_status(self, current_df: pd.DataFrame, features: List[str]) -> Dict:
        """Get overall system health status"""
        # Check drift
        drift_results = self.drift_detector.detect_drift(current_df, features)
        
        # Get performance metrics
        perf_summary = self.performance_tracker.get_performance_summary(hours=24)
        
        # Determine overall health
        health_status = "healthy"
        health_issues = []
        
        if drift_results.get("drift_detected", False):
            health_status = "warning"
            health_issues.append(f"Data drift detected in {drift_results.get('drift_feature_count', 0)} features")
        
        if isinstance(perf_summary, dict) and "latency_stats" in perf_summary:
            if perf_summary["latency_stats"]["p95_ms"] > 100:  # >100ms is concerning
                health_status = "warning" if health_status == "healthy" else "critical"
                health_issues.append("High latency detected (p95 > 100ms)")
            
            if perf_summary.get("anomaly_rate", 0) > 10:  # >10% anomaly rate might indicate issues
                health_issues.append(f"High anomaly rate: {perf_summary['anomaly_rate']:.1f}%")
        
        return {
            "status": health_status,
            "timestamp": datetime.now().isoformat(),
            "issues": health_issues,
            "drift_status": drift_results,
            "performance_status": perf_summary,
            "recommendations": self._generate_recommendations(drift_results, perf_summary)
        }
    
    def _generate_recommendations(self, drift_results: Dict, perf_summary: Dict) -> List[str]:
        """Generate recommendations based on monitoring data"""
        recommendations = []
        
        # Drift-based recommendations
        if drift_results.get("drift_detected", False):
            recommendations.append("Consider retraining model due to data drift")
            
            # Check which features drifted
            for feature, stats in drift_results.get("features", {}).items():
                if stats.get("drift_detected", False):
                    shift = stats.get("mean_shift_pct", 0)
                    if abs(shift) > 20:
                        recommendations.append(
                            f"Significant shift detected in {feature} ({shift:+.1f}%). "
                            f"Investigate data source or business changes."
                        )
        
        # Performance-based recommendations
        if isinstance(perf_summary, dict):
            if perf_summary.get("anomaly_rate", 0) > 15:
                recommendations.append(
                    "Anomaly rate is high. Review model threshold or investigate system issues."
                )
            
            if "latency_stats" in perf_summary:
                if perf_summary["latency_stats"]["p95_ms"] > 100:
                    recommendations.append(
                        "Inference latency is elevated. Consider model optimization or infrastructure scaling."
                    )
        
        if not recommendations:
            recommendations.append("System operating within normal parameters. Continue monitoring.")
        
        return recommendations
