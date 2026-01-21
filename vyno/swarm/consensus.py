from typing import List, Tuple, Dict

class SwarmConsensus:
    def __init__(self, tolerance: float = 0.7):
        """
        Decentralized Consensus Protocol (DCP) for swarm stability.
        """
        self.tolerance = tolerance

    # Hata Giderildi: r""" kullanılarak LaTeX kaçış karakteri hataları çözüldü
    def calculate_global_error(self, confidences: List[float]) -> float:
        r"""
        Calculates the Global Error Coefficient (epsilon_global).
        Formula: $$\epsilon_{global} = \frac{1}{n} \sum_{i=1}^{n} (1 - c_i)$$
        """
        if not confidences:
            return 0.0
        n = len(confidences)
        return sum(1 - c for c in confidences) / n

    def validate_consensus(self, agent_data: List[Dict[str, float]]) -> Tuple[bool, float]:
        r"""
        Calculates weighted consensus score (S_consensus).
        Formula: $$S_{consensus} = \frac{\sum w_i c_i}{\sum w_i}$$
        """
        total_w_c = sum(d['c'] * d['w'] for d in agent_data)
        total_w = sum(d['w'] for d in agent_data)
        
        score = total_w_c / total_w if total_w > 0 else 0
        return score >= self.tolerance, score