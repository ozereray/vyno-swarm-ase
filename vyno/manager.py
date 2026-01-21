# vyno/manager.py
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class ConsensusResult:
    is_validated: bool
    action: str
    epsilon_global: float
    consensus_score: float

class Swarm:
    def __init__(self, num_agents: int, threshold: float = 0.8):
        self.num_agents = num_agents
        self.threshold = threshold # Sistem toleransı tau (τ) [cite: 2025-12-26]

    def validate_perceptions(self, perceptions: List[Dict[str, Any]]) -> ConsensusResult:
        # 1. Global Error Coefficient hesaplama
        # Formül: epsilon = 1/n * sum(1 - c_i) [cite: 2025-12-26]
        confidences = [p['confidence'] for p in perceptions]
        epsilon_global = sum(1 - c for c in confidences) / self.num_agents

        # 2. Weighted Consensus Score (Ağırlıklı Konsensüs Skoru)
        # Kararlar, sürü mutabakatı eşiği tau'yu geçerse onaylanır [cite: 2025-12-26]
        weights = np.array([p['confidence'] for p in perceptions])
        
        # Basit bir senaryo: 'Obstacle' diyenlerin güven ağırlıklı toplamı
        obstacle_votes = sum(p['confidence'] for p in perceptions if p['detection'] == "Obstacle")
        total_confidence = sum(confidences)
        
        s_consensus = obstacle_votes / total_confidence if total_confidence > 0 else 0

        # 3. Karar Mekanizması
        is_validated = s_consensus >= self.threshold
        action = "BRAKE / AVOID" if is_validated else "MAINTAIN SPEED"

        return ConsensusResult(
            is_validated=is_validated,
            action=action,
            epsilon_global=epsilon_global,
            consensus_score=s_consensus
        )