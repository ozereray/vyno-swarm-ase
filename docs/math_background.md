# Mathematical Background: Project VYNO

## 1. Global Error Coefficient

The system calculates system-wide uncertainty using:
$$\epsilon_{global} = \frac{1}{n} \sum_{i=1}^{n} (1 - c_i)$$
where $c_i$ is the confidence score of agent $i$.

## 2. Weighted Consensus Score

Final validation is determined by the score $S_{consensus}$:
$$S_{consensus} = \frac{\sum w_i c_i}{\sum w_i}$$
The system triggers a **Fail-Safe** if $S_{consensus} < \tau$ (threshold).
