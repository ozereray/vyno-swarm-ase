# Step 2: Install in Editable Mode

Installing in editable mode (-e) is essential for developers, as it allows changes in the vyno/ directory to take effect immediately without re-installation:

## 2. Backend Setup

VYNO is designed to be backend-agnostic, supporting industry-standard AI frameworks to power its Perception and Swarm AI layers. You must install the backend that aligns with your specific autonomous use case:

PyTorch Integration: Optimized for research-heavy environments and advanced neural network architectures.

TensorFlow Integration: Recommended for production-scale deployments and high-stability industrial applications.

## 3. Verifying the Setup

To confirm that the VYNO core and your dependencies are correctly initialized, run the following verification command in your terminal:

## 4. Docker Deployment (Optional)

For engineers requiring consistent environments across diverse hardware (e.g., edge computing in automotive systems), VYNO provides a pre-configured Docker setup.

Build the VYNO core Docker image using:

📚 Documentation & Next Steps
Now that your environment is ready, explore the core components of the ecosystem:

System Architecture: Learn about the Perception, Consensus, and Execution layers in .

First Simulation: Launch your first autonomous car swarm by following the .

Mathematical Theory: Deep dive into the error mitigation formulas in the .

Support: If you encounter installation errors or dependency conflicts, please file a report in the GitHub Issues tab.
