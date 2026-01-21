from abc import ABC, abstractmethod
from typing import Dict, Any

class SwarmAgent(ABC):
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.is_active = True

    @abstractmethod
    def process_perception(self, data: Dict[str, Any]):
        """Abstract method to handle raw sensor input."""
        pass

    @abstractmethod
    def compute_trajectory(self, data: Dict[str, Any]):
        """Abstract method to calculate path planning."""
        pass