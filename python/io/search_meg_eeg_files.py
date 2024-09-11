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
from .. import logger, ProjectInfo


# %% ---- 2024-09-09 ------------------------
# Function and class
class MEG_EEG_Files(object):
    links = ProjectInfo.projectRoot.joinpath('data/links.yaml')
    linked_folders = None

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
        folders = [Path(e) for e in links.get('linkedFolders')]
        self.linked_folders = [e for e in folders if e.is_dir()]
        logger.info(f'Found linked_folders: {self.linked_folders}')
        return self.linked_folders

    def search_files(self) -> pd.DataFrame:
        '''
        Search for meg and eeg objects
        It requires everything software pre-installed and make sure the es.exe is in the environment .
        See https://www.voidtools.com/forum/viewtopic.php?t=10176 for details.

        Returns:
            - The DataFrame of the found files, the columns are:
                path, name, suffix, mark
        '''

        def read_files(linked_folder: Path) -> pd.DataFrame:
            # Search all the files using everything
            output = subprocess.check_output(
                args=[
                    'es.exe',  # Using the es.exe
                    '-csv',  # Output CSV format
                    '/a-d',  # Only output files (not directories and others)
                    '-path', linked_folder.as_posix(),  # Only search inside the folder
                    '*',  # I need every file
                ])

            # Re-encode the output into utf-8.
            # ! If there are encoding problems, check this part.
            bytes = output.decode("gbk").encode('utf-8')

            # Make it a data frame
            buffer = io.BytesIO(bytes)
            df = pd.read_csv(buffer)
            df['linkedFolder'] = linked_folder
            return df

        dfs = [read_files(folder) for folder in self.linked_folders]

        df = pd.concat(dfs, axis=0)
        df.index = range(len(df))
        df['path'] = df['Filename'].map(Path)
        df.pop('Filename')
        df['name'] = df['path'].map(lambda d: d.name)
        df['suffix'] = df['path'].map(lambda d: d.suffix)
        df['dataType'] = 'N.A.'
        self.files = df

        # Parse the files by name
        self.parse_files_by_name()

        return self.files

    def parse_files_by_name(self):
        '''
        Several parsing operations.
        '''
        self._parse_data_for_bdf_files()
        return

    def _parse_data_for_bdf_files(self):
        '''
        Find and mark .bdf files.

        It supposes the .bdf file are in pair.
        - data.bdf, is the data file.
        - evt.bdf, in the same folder, is the event file.

        ```python
        # Read and link them in mne package
        raw = mne.io.read_raw('data.bdf')
        annotations = mne.read_annotations('evt.bdf')
        raw.set_annotations(annotations)
        ```

        The .bdf format document:
        - https://mne.tools/stable/auto_tutorials/io/20_reading_eeg_data.html
        - https://www.biosemi.com/faq/file_format.htm

        BioSemi data format (.bdf)

        The BDF format is a 24-bit variant of the EDF format used by EEG systems manufactured by BioSemi. It can be imported with mne.io.read_raw_bdf().
        BioSemi amplifiers do not perform “common mode noise rejection” automatically. The signals in the EEG file are the voltages between each electrode and the CMS active electrode, which still contain some CM noise (50 Hz, ADC reference noise, etc.). The BioSemi FAQ provides more details on this topic. Therefore, it is advisable to choose a reference (e.g., a single channel like Cz, average of linked mastoids, average of all electrodes, etc.) after importing BioSemi data to avoid losing signal information. The data can be re-referenced later after cleaning if desired.
        '''
        # Only work with the rows marked by N.A.
        qp = 'dataType=="N.A."'

        # The column name for the data type
        data_type_column = 'dataType'

        # Drop the evt.bdf files since it is used by its data.bdf
        query = ' & '.join([qp, 'name == "evt.bdf"'])
        before = len(self.files)
        self.files.drop(self.files.query(query).index, inplace=True)
        after = len(self.files)
        logger.debug(f'Dropped evt.bdf files: [{before}] -> [{after}]')

        # Find data.bdf files
        query = ' & '.join([qp, 'name == "data.bdf"'])
        df = self.files.query(query)
        self.files.loc[df.index, data_type_column] = 'bdf'
        logger.debug(f'Found .bdf files: {len(df)}')

        # Mark abnormal .bdf files
        query = ' & '.join([qp, 'suffix == ".bdf"'])
        df = self.files.query(query)
        self.files.loc[df.index, data_type_column] = 'bdf (abnormal)'
        logger.debug(f'Found abnormal .bdf files: {len(df)}')
        return


# %% ---- 2024-09-09 ------------------------
# Play ground


# %% ---- 2024-09-09 ------------------------
# Pending


# %% ---- 2024-09-09 ------------------------
# Pending
