"""
Model Registry for GreenLens AI
Tracks model versions, metadata, and performance metrics
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import pickle


class ModelRegistry:
    """Manages model versions, metadata, and history"""
    
    def __init__(self, registry_path: str = "models/registry.json"):
        self.registry_path = registry_path
        self.models_dir = os.path.dirname(registry_path)
        self._ensure_directories()
        self.registry = self._load_registry()
    
    def _ensure_directories(self):
        """Create necessary directories"""
        os.makedirs(self.models_dir, exist_ok=True)
        os.makedirs("logs", exist_ok=True)
    
    def _load_registry(self) -> Dict:
        """Load registry from JSON file"""
        if os.path.exists(self.registry_path):
            with open(self.registry_path, 'r') as f:
                return json.load(f)
        return {
            "models": [],
            "current_version": None,
            "created_at": datetime.now().isoformat()
        }
    
    def _save_registry(self):
        """Save registry to JSON file"""
        with open(self.registry_path, 'w') as f:
            json.dump(self.registry, f, indent=2)
    
    def register_model(
        self, 
        model_object,
        version: str,
        parameters: Dict,
        performance_metrics: Dict,
        training_data_stats: Dict,
        description: str = "",
        tags: List[str] = None
    ) -> str:
        """
        Register a new model version
        
        Args:
            model_object: The trained model (pickled)
            version: Version string (e.g., "v1.0.0")
            parameters: Model hyperparameters
            performance_metrics: Model performance metrics
            training_data_stats: Statistics about training data
            description: Human-readable description
            tags: List of tags for categorization
        
        Returns:
            model_id: Unique identifier for the model
        """
        model_id = f"model_{version}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        model_path = os.path.join(self.models_dir, f"{model_id}.pkl")
        
        # Save model object
        with open(model_path, 'wb') as f:
            pickle.dump(model_object, f)
        
        # Create model metadata
        model_entry = {
            "model_id": model_id,
            "version": version,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "model_path": model_path,
            "parameters": parameters,
            "performance_metrics": performance_metrics,
            "training_data_stats": training_data_stats,
            "tags": tags or [],
            "status": "active",
            "deployment_history": []
        }
        
        # Add to registry
        self.registry["models"].append(model_entry)
        self.registry["current_version"] = model_id
        self._save_registry()
        
        return model_id
    
    def get_model(self, model_id: str = None) -> tuple:
        """
        Load a model by ID or return current model
        
        Args:
            model_id: Model identifier (None = current version)
        
        Returns:
            (model_object, metadata)
        """
        if model_id is None:
            model_id = self.registry["current_version"]
        
        if not model_id:
            return None, None
        
        # Find model metadata
        model_entry = None
        for model in self.registry["models"]:
            if model["model_id"] == model_id:
                model_entry = model
                break
        
        if not model_entry:
            return None, None
        
        # Load model object
        with open(model_entry["model_path"], 'rb') as f:
            model_object = pickle.load(f)
        
        return model_object, model_entry
    
    def get_model_history(self) -> List[Dict]:
        """Get all model versions sorted by date (newest first)"""
        return sorted(
            self.registry["models"], 
            key=lambda x: x["created_at"], 
            reverse=True
        )
    
    def set_current_version(self, model_id: str):
        """Set the active model version"""
        self.registry["current_version"] = model_id
        self._save_registry()
    
    def log_deployment(self, model_id: str, environment: str, notes: str = ""):
        """Log a deployment event"""
        for model in self.registry["models"]:
            if model["model_id"] == model_id:
                deployment_record = {
                    "timestamp": datetime.now().isoformat(),
                    "environment": environment,
                    "notes": notes
                }
                model["deployment_history"].append(deployment_record)
                self._save_registry()
                break
    
    def get_latest_metrics(self) -> Optional[Dict]:
        """Get metrics for the current model version"""
        _, metadata = self.get_model()
        if metadata:
            return metadata.get("performance_metrics", {})
        return None
    
    def compare_versions(self, model_id_1: str, model_id_2: str) -> Dict:
        """Compare two model versions"""
        _, meta1 = self.get_model(model_id_1)
        _, meta2 = self.get_model(model_id_2)
        
        if not meta1 or not meta2:
            return {"error": "One or both models not found"}
        
        return {
            "model_1": {
                "id": model_id_1,
                "version": meta1["version"],
                "created_at": meta1["created_at"],
                "metrics": meta1["performance_metrics"]
            },
            "model_2": {
                "id": model_id_2,
                "version": meta2["version"],
                "created_at": meta2["created_at"],
                "metrics": meta2["performance_metrics"]
            },
            "comparison": {
                "latency_diff": meta2["performance_metrics"].get("latency_ms", 0) - 
                               meta1["performance_metrics"].get("latency_ms", 0),
                "confidence_diff": meta2["performance_metrics"].get("confidence", 0) - 
                                  meta1["performance_metrics"].get("confidence", 0)
            }
        }
