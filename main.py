import numpy as np
from vyno.core.engine import AutonomousEngine
from vyno.swarm.consensus import SwarmConsensus
from vyno.swarm.manager import SwarmManager
from vyno.core.execution import ExecutionLayer

def start_vyno_ecosystem():
    print("--- VYNO Autonomous Swarm Ecosystem Initializing ---")
    
    # 1. Initialize Agents and System Components
    # Vision: Eliminate single-point failures through a decentralized architecture [cite: 2025-12-26]
    # This aligns with Germany's leadership in high-quality mobility standards [cite: 2025-12-06]
    agents = [AutonomousEngine(agent_id=f"Drone_{i}") for i in range(1, 4)]
    consensus_protocol = SwarmConsensus(tolerance=0.75)
    manager = SwarmManager(agents, consensus_protocol)
    executor = ExecutionLayer(safety_threshold=0.80)

    # 2. Simulate Sample Sensor Data
    # This represents real-world environmental perception for autonomous navigation [cite: 2025-12-26]
    sensor_input = {"environment_status": "detecting_obstacle"}

    # 3. Execute Swarm Cycle (Perception -> Consensus)
    # Mathematical Foundation: The Global Error Coefficient measures swarm uncertainty [cite: 2025-12-26]
    # Calculated as: $\epsilon_{global} = \frac{1}{n} \sum (1 - c_i)$
    swarm_decision = manager.process_swarm_cycle(sensor_input)

    # 4. Relay Decision to the Execution Layer
    # Logic: Commands are only authorized if the weighted consensus score exceeds the threshold [cite: 2025-12-26]
    # Execution Condition: $S_{consensus} \geq \tau$
    success = executor.execute(swarm_decision, command="OBSTACLE_AVOIDANCE_LEFT")

    print(f"\n--- Cycle Results ---")
    print(f"Validated: {swarm_decision['is_validated']}")
    print(f"Consensus Score: {swarm_decision['consensus_score']:.4f}")
    print(f"Final Status: {'SAFE - OPERATION EXECUTED' if success else 'HALTED - FAILSAFE TRIGGERED'}")

if __name__ == "__main__":
    # Start the VYNO system cycle [cite: 2025-12-26]
    start_vyno_ecosystem()