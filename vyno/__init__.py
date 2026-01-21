# vyno/__init__.py
try:
    from vyno.manager import Swarm
except ImportError:
    from .manager import Swarm

__version__ = "1.0.0"