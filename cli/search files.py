"""
File: search files.py
Author: Chuncheng Zhang
Date: 2024-09-09
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Command line interface for searching for files.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-09-09 ------------------------
# Requirements and constants
from python.io.search_meg_eeg_files import MEG_EEG_Files
from rich import print


# %% ---- 2024-09-09 ------------------------
# Function and class


# %% ---- 2024-09-09 ------------------------
# Play ground
if __name__ == "__main__":
    mef = MEG_EEG_Files()
    mef.search_files()
    group = mef.files
    print(mef.files)
    group = mef.files.groupby(['linkedFolder', 'dataType', 'suffix'])
    print(group.count())


# %% ---- 2024-09-09 ------------------------
# Pending


# %% ---- 2024-09-09 ------------------------
# Pending
