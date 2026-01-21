# API Reference

Detailed technical documentation for the core VYNO classes.

### `vyno.swarm.consensus.SwarmConsensus`

The main controller for swarm-level decision validation.

- **`__init__(tolerance_level: float)`**: Sets the minimum required confidence for the swarm.
- **`validate_swarm_decisions(swarm_outputs: List[Dict])`**: Returns a boolean validation status and a detailed error report.

### `vyno.agents.base.BaseAgent`

An abstract class for all autonomous units.

- **`perceive()`**: Input method for environment data.
- **`act()`**: Decision-making logic.
