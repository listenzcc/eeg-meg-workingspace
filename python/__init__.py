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
import os
from pathlib import Path
from loguru import logger


# %% ---- 2024-09-09 ------------------------
# Function and class
class ProjectInfo:
    projectName = 'EEG MEG WorkingSpace'
    version = '0.1'
    # The folder containing python/__init__.py(this file)
    projectRoot = Path(__file__).parent.parent


# %% ---- 2024-09-09 ------------------------
# Play ground
logger.add(
    Path(
        os.environ.get('HOME', '.'),
        'log/{}.log'.format(ProjectInfo.projectName)),
    rotation='5 MB')


# %% ---- 2024-09-09 ------------------------
# Pending


# %% ---- 2024-09-09 ------------------------
# Pending
