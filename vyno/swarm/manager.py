from typing import List, Dict, Any
from vyno.core.engine import AutonomousEngine
from vyno.swarm.consensus import SwarmConsensus

class SwarmManager:
    def __init__(self, agents: List[AutonomousEngine], consensus_module: SwarmConsensus):
        """
        Coordinates multiple autonomous agents to reach a swarm-level decision.
       
        """
        self.agents = agents
        self.consensus_module = consensus_module

    def process_swarm_cycle(self, sensor_stream: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes a full cycle: Perception -> Consensus.
        """
        swarm_payload = []
        
        # 1. Perception Layer: Collect confidence scores from all agents
        for agent in self.agents:
            _, confidence = agent.process_perception(sensor_stream)
            # Default weight (w) is 1.0; can be adjusted based on agent reliability
            swarm_payload.append({"c": confidence, "w": 1.0})

        # 2. Consensus Layer: Validate the global decision
        is_validated, score = self.consensus_module.validate_consensus(swarm_payload)
        
        return {
            "is_validated": is_validated,
            "consensus_score": score,
            "agent_count": len(self.agents)
        }