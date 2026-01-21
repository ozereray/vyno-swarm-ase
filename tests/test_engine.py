import pytest
from vyno.core.engine import AutonomousEngine

def test_engine_initialization():
    """
    Motorun config ile veya config olmadan 
    sorunsuz başlatıldığını doğrular.
    """
    # Senaryo 1: config={} göndererek başlatma
    engine_a = AutonomousEngine(agent_id="A1", config={})
    assert engine_a.agent_id == "A1"
    
    # Senaryo 2: Parametre göndermeden başlatma (Optional[Dict] testi)
    engine_b = AutonomousEngine(agent_id="B1")
    assert engine_b.agent_id == "B1"
    assert isinstance(engine_b.config, dict)

def test_trajectory_format():
    """
    Hesaplanan yörüngenin beklenen liste (list) 
    formatında olduğunu kontrol eder.
    """
    engine = AutonomousEngine(agent_id="A1")
    traj = engine.compute_trajectory({})
    
    assert isinstance(traj, list)
    assert len(traj) > 0