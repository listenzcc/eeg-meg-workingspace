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
import io
import subprocess
import pandas as pd

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

    def search_files(self) -> pd.DataFrame:
        '''
        Search for meg and eeg objects
        It requires everything software pre-installed and make sure the es.exe is in the environment .
        See https://www.voidtools.com/forum/viewtopic.php?t=10176 for details.

        Returns:
            - The DataFrame of the found files, the columns are:
                path, name, suffix, mark
        '''
        # Search all the files using everything
        output = subprocess.check_output(
            args=['es.exe', '-csv', '/a-d', '-path', 'D:\\脑机接口专项', '*'])

        # Re encode the output into utf-8
        bytes = output.decode("gbk").encode('utf-8')
        buffer = io.BytesIO(bytes)

        # Make it a data frame
        df = pd.read_csv(buffer)
        df['path'] = df['Filename'].map(Path)
        df.pop('Filename')
        df['name'] = df['path'].map(lambda d: d.name)
        df['suffix'] = df['path'].map(lambda d: d.suffix)
        df['fileMark'] = 'N.A.'
        self.files = df

        # Parse the files by name
        self.parse_files_by_name()

        return self.files

    def parse_files_by_name(self):
        '''
        Several parsing operations.
        '''
        self._parse_data_for_bdf_files()

    def _parse_data_for_bdf_files(self):
        '''
        Find and mark .bdf files.
        '''
        # Only work with the rows marked by N.A.
        qp = 'fileMark=="N.A."'

        # Drop the evt.bdf files since it is used by its data.bdf
        query = ' & '.join([qp, 'name == "evt.bdf"'])
        before = len(self.files)
        self.files.drop(self.files.query(query).index, inplace=True)
        after = len(self.files)
        logger.debug(f'Dropped evt.bdf files: [{before}] -> [{after}]')

        # Find data.bdf files
        query = ' & '.join([qp, 'name == "data.bdf"'])
        df = self.files.query(query)
        self.files.loc[df.index, 'mark'] = 'bdf'
        logger.debug(f'Found .bdf files: {len(df)}')

        # Mark abnormal .bdf files
        query = ' & '.join([qp, 'suffix == ".bdf"'])
        df = self.files.query(query)
        self.files.loc[df.index, 'mark'] = 'bdf (abnormal)'
        logger.debug(f'Found abnormal .bdf files: {len(df)}')
        return


# %% ---- 2024-09-09 ------------------------
# Play ground


# %% ---- 2024-09-09 ------------------------
# Pending


# %% ---- 2024-09-09 ------------------------
# Pending
