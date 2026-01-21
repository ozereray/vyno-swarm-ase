import numpy as np
from vyno.swarm.consensus import SwarmConsensus
from vyno.core.engine import AutonomousEngine

# Hata Giderildi: 'tolerance_level' yerine 'tolerance' kullanıldı
swarm_manager = SwarmConsensus(tolerance=0.75)

# Ajan simülasyonu
agent = AutonomousEngine(agent_id="Agent_01")
sensor_data = {"lidar": np.random.rand(360)}
_, confidence = agent.process_perception(sensor_data)

# Karar verisi hazırlama
decision_data = [{"c": confidence, "w": 1.0}]

# Hata Giderildi: 'validate_swarm_decisions' yerine 'validate_consensus' kullanıldı
is_safe, consensus_score = swarm_manager.validate_consensus(decision_data)

if is_safe:
    print(f"Decision Validated. Score: {consensus_score:.2f}")
else:
    print("Re-evaluation Protocol Triggered.")