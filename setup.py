from setuptools import setup, find_packages

setup(
    name="vyno-swarm-ase",
    version="1.0.0",
    author="Eray Özer",
    description="A Decentralized Autonomous Swarm Ecosystem framework",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.8',
)