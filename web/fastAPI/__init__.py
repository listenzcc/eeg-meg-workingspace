"""
File: __init__.py
Author: Chuncheng Zhang
Date: 2024-09-10
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-09-10 ------------------------
# Requirements and constants
import os
from pathlib import Path
from loguru import logger


# %% ---- 2024-09-10 ------------------------
# Function and class

class ProjectInfo:
    projectName = 'EEG MEG WorkingSpace (FastAPI)'
    version = 'V0.1'
    # The folder containing fastAPI/__init__.py
    # It also contains the 'src' folder
    webRoot = Path(__file__).parent.parent
    # The folder containing the 'webRoot' and 'python'
    projectRoot = webRoot.parent
    # The folder containing the md contents
    contentRoot = projectRoot.joinpath('content')


# %% ---- 2024-09-10 ------------------------
# Play ground
logger.add(
    Path(
        os.environ.get('HOME', '.'),
        'log/{}.log'.format(ProjectInfo.projectName)),
    rotation='5 MB')

# %% ---- 2024-09-10 ------------------------
# Pending


# %% ---- 2024-09-10 ------------------------
# Pending
