"""
File: search-meg-eeg-files.py
Author: Chuncheng Zhang
Date: 2024-09-09
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Search for meg or eeg files.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-09-09 ------------------------
# Requirements and constants
import subprocess
from pathlib import Path
from omegaconf import OmegaConf
from .. import logger, project_root


# %% ---- 2024-09-09 ------------------------
# Function and class
class MEG_EEG_Files(object):
    links = project_root.joinpath('data/links.yaml')
    folders = None

    def __init__(self):
        self.get_linked_folders()
        logger.info('Initialized')

    def get_linked_folders(self) -> list[Path]:
        '''
        Get the linked folders.

        Returns:
            - list of folders
        '''
        links = OmegaConf.load(self.links)
        folders = [Path(e) for e in links.get('dataFolders')]
        self.folders = [e for e in folders if e.is_dir()]
        logger.info(f'Found linked folders: {self.folders}')
        return self.folders

    def search_objs(self):
        '''
        Search for meg and eeg objects
        It requires everything software pre-installed.
        '''
        found = subprocess.call(args=['es.exe', '-path', 'D:\\脑机接口专项', '*'])
        print(found)


# %% ---- 2024-09-09 ------------------------
# Play ground
if __name__ == "__main__":
    mef = MEG_EEG_Files()
    mef.get_linked_folders()


# %% ---- 2024-09-09 ------------------------
# Pending


# %% ---- 2024-09-09 ------------------------
# Pending
