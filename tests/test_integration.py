import pytest
from vyno.core.engine import AutonomousEngine
from vyno.swarm.consensus import SwarmConsensus
from vyno.swarm.manager import SwarmManager
from vyno.core.execution import ExecutionLayer

def test_full_system_validation_flow():
    # 1. Setup components
    agents = [AutonomousEngine(agent_id=f"Agent_{i}") for i in range(3)]
    consensus = SwarmConsensus(tolerance=0.7)
    manager = SwarmManager(agents, consensus)
    executor = ExecutionLayer(safety_threshold=0.7)
    
    # 2. Simulate sensor data and process cycle
    sensor_data = {"environment": "standard_road"}
    swarm_decision = manager.process_swarm_cycle(sensor_data)
    
    # 3. Test execution gate
    # Assuming default engine confidence is 0.95 (from our previous engine.py)
    result = executor.execute(swarm_decision, "MOVE_FORWARD")
    
    assert swarm_decision["is_validated"] is True
    assert result is True

def test_fail_safe_on_low_consensus():
    # Setup with high tolerance to trigger fail-safe
    agents = [AutonomousEngine(agent_id="A1")]
    consensus = SwarmConsensus(tolerance=0.99) # Extremely high bar
    manager = SwarmManager(agents, consensus)
    executor = ExecutionLayer(safety_threshold=0.99)
    
    swarm_decision = manager.process_swarm_cycle({})
    result = executor.execute(swarm_decision, "ACCELERATE")
    
    assert result is False # Must be blocked