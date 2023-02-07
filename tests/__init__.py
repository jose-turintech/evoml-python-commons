"""
The application is initialized with the testing configuration
"""
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
from pathlib import Path

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                             Global testing configuration                                             #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

TESTS_PATH: Path = Path(__file__).parent
ROOT_PATH: Path = TESTS_PATH.parent
