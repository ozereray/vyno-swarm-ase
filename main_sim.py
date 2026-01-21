import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from vyno.manager import Swarm

# 1. Swarm and Simulation Configuration
# num_agents: 8, threshold (tau): 0.75 for robust consensus [cite: 2025-12-26]
num_agents = 8
swarm = Swarm(num_agents=num_agents, threshold=0.75)
fig, ax = plt.subplots(figsize=(10, 7))

def update(frame):
    """
    Update function for the animation. 
    Simulates a 20-frame cycle with a recovery phase.
    """
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.set_title("Project VYNO: Decentralized Consensus & Self-Healing Simulation")
    
    # Obstacle simulation (Static red line representing a sensor detection point)
    ax.axvline(x=8, color='red', linestyle='--', label='Obstacle')
    
    # 2. Chaos vs. Recovery Logic
    # Every 20 frames, we simulate a 'Chaos Phase' for 5 frames where 
    # multiple agents provide conflicting data simultaneously.
    current_cycle_frame = frame % 20
    is_chaos_phase = 10 <= current_cycle_frame <= 15
    
    perceptions = []
    for i in range(num_agents):
        # Scenario: Massive failure during interference, otherwise only Agent 0 is an outlier
        if is_chaos_phase and i < 5: 
            # 5 agents 'fail' at once, dropping below the consensus threshold
            conf, det = 0.2, "Clear Path" 
        elif i == 0: 
            # Agent 0 is a constant outlier to test Byzantine Fault Tolerance (BFT) [cite: 2025-12-26]
            conf, det = 0.3, "Clear Path"
        else:
            # Healthy agents detecting the actual obstacle
            conf, det = 0.9, "Obstacle"
            
        perceptions.append({"agent_id": i, "detection": det, "confidence": conf})
        
        # Visualize agents moving towards the obstacle
        # Color coding: Green (Healthy), Red (Systemic Failure), Orange (Individual Outlier)
        if is_chaos_phase and i < 5:
            color = 'red'
        elif i == 0:
            color = 'orange'
        else:
            color = 'green'
            
        x_pos = current_cycle_frame % 9 # Loop movement
        ax.scatter(x_pos, i + 1, c=color, s=150, edgecolors='black', zorder=3)
        ax.text(x_pos, i + 1.3, f"Ag {i}\nC:{conf}", fontsize=8, ha='center')

    # 3. Execute Decentralized Consensus Protocol (DCP) [cite: 2025-12-26]
    result = swarm.validate_perceptions(perceptions)
    
    # 4. Dynamic UI Feedback
    status_text = "STATUS: CONSENSUS VALIDATED" if result.is_validated else "STATUS: SYSTEM FAILURE - REPAIRING..."
    status_color = "green" if result.is_validated else "red"
    
    # Display results and mathematical coefficients [cite: 2025-12-26]
    ax.text(0.5, 10.2, status_text, color=status_color, fontweight='bold', fontsize=12)
    ax.text(0.5, 9.7, f"Global Error Coefficient (ε): {result.epsilon_global:.3f}")
    ax.text(0.5, 9.2, f"Weighted Consensus Score (S): {result.consensus_score:.3f}")
    ax.text(7.5, 10.2, f"Decision:\n{result.action}", bbox=dict(facecolor='white', alpha=0.5))

    # Return empty list to resolve Pylance Iterable[Artist] error
    return []

# 5. Animation Control
# Save this to assets/demo.gif after running
ani = animation.FuncAnimation(fig, update, frames=40, interval=400, blit=False)

# Optional: To save directly, uncomment the line below (requires 'pillow' library)
# ani.save('assets/demo.gif', writer='pillow', fps=2.5)

plt.tight_layout()
plt.show()