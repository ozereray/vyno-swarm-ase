import vyno
import numpy as np

# 1. Initialize the Swarm Ecosystem
# Simulating 5 agents with a consensus threshold of 0.85
swarm = vyno.Swarm(num_agents=5, threshold=0.85)

# 2. Simulate Perception Data
# In a real scenario, these would come from LIDAR/Camera sensors
perceptions = [
    {"agent_id": 0, "detection": "Obstacle", "confidence": 0.95},
    {"agent_id": 1, "detection": "Obstacle", "confidence": 0.92},
    {"agent_id": 2, "detection": "Clear Path", "confidence": 0.40},  # Potential outlier/malfunction
    {"agent_id": 3, "detection": "Obstacle", "confidence": 0.88},
    {"agent_id": 4, "detection": "Obstacle", "confidence": 0.90}
]

# 3. Apply the Consensus Layer
# This calculates the Weighted Consensus Score (S_consensus)
# and rejects outliers automatically
result = swarm.validate_perceptions(perceptions)

if result.is_validated:
    print(f"Action Executed: {result.action}")
    print(f"Global Error Coefficient: {result.epsilon_global:.4f}")
else:
    print("Safety Gate Triggered: Consensus not reached.")