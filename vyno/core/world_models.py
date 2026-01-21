import numpy as np
from typing import Dict, Any, Optional, Tuple

class WorldModel:
    def __init__(self, physics_config: Optional[Dict[str, Any]] = None):
        """
        World Model for predictive autonomy and environmental simulation.
        [cite: 2025-12-26]
        
        Args:
            physics_config: Optional dictionary for physical constants.
        """
        # Hata Giderildi: Optional[Dict] kullanılarak None ataması güvenli hale getirildi
        self.config = physics_config if physics_config is not None else {"gravity": 9.81, "friction": 0.5}
        self.state_history = []

    def predict_next_state(self, current_state: np.ndarray, action: np.ndarray) -> np.ndarray:
        r"""
        Predicts the next state based on current state and applied action.
        Formula: $$s_{t+1} = \mathcal{M}(s_t, a_t)$$
        """
        # Basit doğrusal tahmin mantığı
        prediction = current_state + action * self.config["friction"]
        return prediction

    def calculate_prediction_error(self, predicted_state: np.ndarray, actual_state: np.ndarray) -> float:
        """
        Calculates the Euclidean distance between prediction and reality.
        """
        error = np.linalg.norm(predicted_state - actual_state)
        return float(error)

    def get_physical_consistency_score(self, error: float) -> float:
        """
        Converts prediction error into a consistency score [0, 1].
        """
        return max(0.0, 1.0 - (error / 10.0))