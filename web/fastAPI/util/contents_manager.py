"""
File: contents_manager.py
Author: Chuncheng Zhang
Date: 2024-09-12
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


# %% ---- 2024-09-12 ------------------------
# Requirements and constants
import os
from omegaconf import OmegaConf
from pathlib import Path
from .. import logger


# %% ---- 2024-09-12 ------------------------
# Function and class
def read_md_file(path: Path):
    content = open(path, encoding="utf-8").read()
    m_block = guess_md_metadata_block(content)

    # If the content starts with the yaml metadata block,
    # remove it from the content.
    if content.startswith('---'):
        content = content.split('---', 2)[-1]

    m_block.update({'content': content})
    logger.debug(f'Read md file: {path}')
    return m_block


def guess_md_metadata_block(content: str):
    '''
    Only accept the heading comments for the md file.
    It is the yaml_metadata_block by pandoc.
    https://pandoc.org/MANUAL.html#extension-yaml_metadata_block

    ---
    Key1: value
    Key2: value
    Key3: value
    ...
    (The values inside the block is the heading comments)
    ---

    .... Other contents ...

    '''
    # Fail on not starting with '---'
    if not content.strip().startswith('---'):
        return {}

    # Fail on empty content
    if not (split := [e for e in content.split('---') if e.strip()]):
        return {}

    # Parse the heading comments (hc)
    # Fail on cannot converting
    try:
        return OmegaConf.create(split[0])
    except Exception:
        return {}


def search_contents(folder: Path):
    '''
    Search the contents in the given folder

    Args:
        - folder: Path of the searching folder

    Returns:
        - The list of the contents in the dict,
            the columns are 'path', 'author', 'title', 'date'
    '''

    assert folder.is_dir(), f'Invalid folder: {folder}'

    found = []
    for parent, _, names in os.walk(folder):
        for name in [e for e in names if e.endswith('.md')]:
            p = Path(parent, name)
            content = open(p, encoding="utf-8").read()

            m_block = guess_md_metadata_block(content)
            logger.debug(f'Parsed heading comments: {m_block}')

            dct = dict(
                path=p.relative_to(folder).as_posix(),
                author=m_block.get('Author', 'N.A.'),
                title=m_block.get('Title', 'N.A.'),
                date=m_block.get('Date', 'N.A.')
            )

            found.append(dct)
            logger.debug(f'Found file: {found[-1]}')

    return found


# %% ---- 2024-09-12 ------------------------
# Play ground


# %% ---- 2024-09-12 ------------------------
# Pending


# %% ---- 2024-09-12 ------------------------
# Pending
