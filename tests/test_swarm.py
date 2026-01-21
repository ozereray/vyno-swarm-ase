import pytest
from vyno.swarm.consensus import SwarmConsensus

def test_swarm_initialization():
    # Artık 'tolerance' ismiyle çağırıyoruz
    swarm = SwarmConsensus(tolerance=0.85)
    assert swarm.tolerance == 0.85

def test_consensus_logic():
    swarm = SwarmConsensus(tolerance=0.7)
    data = [{"c": 0.6, "w": 1.0}, {"c": 0.5, "w": 1.0}] # Ortalama 0.55 < 0.7
    is_valid, _ = swarm.validate_consensus(data)
    assert is_valid is False