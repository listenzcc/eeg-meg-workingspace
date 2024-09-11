"""
File: app.py
Author: Chuncheng Zhang
Date: 2024-09-10
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    FastAPI application with routines.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-09-10 ------------------------
# Requirements and constants
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path
from typing import Annotated

from . import logger, ProjectInfo


# %% ---- 2024-09-10 ------------------------
# Function and class
class WebApp(FastAPI):
    src_directory = ProjectInfo.webRoot.joinpath('src')
    jinja2_templates: Jinja2Templates

    def __init__(self):
        super(WebApp, self).__init__(title='{}, {}'.format(
            ProjectInfo.projectName, ProjectInfo.version))

        self.mount_path()
        self.bind_jinja2_templates()
        logger.debug(f'Initialized with {self.title}')

    def mount_path(self):
        '''
        Mount path(request url) to directory(local directory)
        '''
        kwargs = dict(
            name='static', path='/static',
            app=StaticFiles(directory=self.src_directory.joinpath('static')))
        self.mount(**kwargs)
        logger.debug(f'Mounted with {kwargs}')
        return

    def bind_jinja2_templates(self):
        '''Bind with the jinja2 templates'''
        directory = self.src_directory.joinpath('templates')
        self.jinja2_templates = Jinja2Templates(directory=directory)
        logger.debug(
            f'Binned with the jinja2 templates directory: {directory}')
        return

    def something_is_wrong(self, exception, custom_message=None):
        '''
        Fetch the details when something is wrong.

        Args:
            - exception: The exception.
            - custom_message: The custom message for the exception.

        Returns:
            - detail(dict): The detail of the exception.
        '''
        import traceback
        detail = traceback.format_exc()
        logger.error(exception)
        print(detail)
        return dict(
            exception=f'{exception}',
            detail=detail,
            customMessage=custom_message
        )


# ----------------------------------------
# ---- Must initialize the app in the first place ----
wa = WebApp()


# %% ---- 2024-09-10 ------------------------
# Play ground

# ----------------------------------------
# ---- Routine ----
@wa.get('/')
async def index(request: Request):
    '''Homepage'''
    context = {'request': request}
    return wa.jinja2_templates.TemplateResponse('index.html', context)


@wa.get('/getDoc')
async def get_doc(request: Request, relPath: str):
    print(relPath)
    p = ProjectInfo.webRoot.joinpath('doc', relPath)

    if not p.is_file():
        raise HTTPException(status_code=404, detail='File not found')

    try:
        content = open(p, encoding='utf-8').read()
        return dict(content=content)
    except Exception as exc:
        raise HTTPException(
            status_code=404, detail=wa.something_is_wrong(exc)
        ) from exc


# %% ---- 2024-09-10 ------------------------
# Pending


# %% ---- 2024-09-10 ------------------------
# Pending
