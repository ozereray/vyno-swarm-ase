import pytest
import numpy as np
from vyno.core.engine import AutonomousEngine
from vyno.swarm.consensus import SwarmConsensus
from vyno.swarm.manager import SwarmManager

def test_single_agent_failure_resilience():
    r"""
    Scenario: 1 out of 3 agents produces a low confidence score (faulty sensor).
    Goal: The swarm consensus score (S_consensus) should remain above the tolerance threshold. 
    """
    # Initialize components
    agents = [AutonomousEngine(agent_id=f"Agent_{i}") for i in range(3)]
    consensus = SwarmConsensus(tolerance=0.7)
    manager = SwarmManager(agents, consensus)

    # Simulation: High confidence for agents 1 & 2, low confidence for agent 3
    sensor_data = {"state": np.array([10.0, 5.0, 1.0])}
    
    swarm_payload = []
    for i, agent in enumerate(agents):
        _, confidence = agent.process_perception(sensor_data)
        # Manually override the 3rd agent's confidence to simulate failure
        if i == 2:
            confidence = 0.3 # Critical failure simulation
        swarm_payload.append({"c": confidence, "w": 1.0})

    # Validate consensus
    is_validated, score = consensus.validate_consensus(swarm_payload)
    
    # Mathematical Verification: (0.95 + 0.95 + 0.3) / 3 = ~0.73
    assert is_validated is True
    assert score >= 0.7

def test_majority_failure_trigger_failsafe():
    r"""
    Scenario: Majority of the swarm (2/3) produces faulty data.
    Goal: The system must reject consensus and trigger the fail-safe protocol. 
    """
    agents = [AutonomousEngine(agent_id=f"A_{i}") for i in range(3)]
    consensus = SwarmConsensus(tolerance=0.8) # High safety threshold
    
    # Majority failure simulation
    faulty_payload = [
        {"c": 0.4, "w": 1.0}, # Faulty
        {"c": 0.5, "w": 1.0}, # Faulty
        {"c": 0.95, "w": 1.0} # Healthy
    ]
    
    is_validated, score = consensus.validate_consensus(faulty_payload)
    
    assert is_validated is False
    assert score < 0.8

def test_global_error_coefficient_consistency():
    r"""
    Verifies the Global Error Coefficient formula under total system failure.
    Formula: $$\epsilon_{global} = \frac{1}{n} \sum_{i=1}^{n} (1 - c_i)$$
    """
    swarm = SwarmConsensus()
    # Scenario: All agents report 0 confidence
    total_failure_confidences = [0.0, 0.0, 0.0]
    
    epsilon = swarm.calculate_global_error(total_failure_confidences)
    
    # If all agents are at 0, epsilon_global must be 1.0 (maximum error) 
    assert epsilon == 1.0