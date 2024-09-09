"""
File: __init__.py
Author: Chuncheng Zhang
Date: 2024-09-09
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Initialization for the python module.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-09-09 ------------------------
# Requirements and constants
from pathlib import Path
from omegaconf import OmegaConf

from loguru import logger

# The folder containing the python and data subdirectories.
project_root = Path(__file__).parent.parent
logger.add(
    project_root.joinpath('log/eeg-meg-workingspace.log'),
    rotation='5 MB')

# %% ---- 2024-09-09 ------------------------
# Function and class


# %% ---- 2024-09-09 ------------------------
# Play ground


# %% ---- 2024-09-09 ------------------------
# Pending


# %% ---- 2024-09-09 ------------------------
# Pending
