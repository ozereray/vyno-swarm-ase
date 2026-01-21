class ExecutionLayer:
    def __init__(self, safety_threshold: float = 0.75):
        """
        Final safety gate for autonomous actions.
        Ensures near-zero error rates by blocking non-validated swarm decisions.
        """
        self.threshold = safety_threshold

    def execute(self, swarm_result: dict, command: str) -> bool:
        """
        Permits or blocks the command based on the consensus score.
        """
        if swarm_result.get("is_validated") and swarm_result.get("consensus_score", 0) >= self.threshold:
            print(f"[EXECUTION] Command '{command}' PERMITTED. Score: {swarm_result['consensus_score']:.2f}")
            return True
        else:
            print(f"[EXECUTION] Command '{command}' BLOCKED. Fail-safe activated.")
            return False