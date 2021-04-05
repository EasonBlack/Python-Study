"""
python3 setup.py py2app
dist/demo1.app/Contents/MacOS/demo1
"""

from setuptools import setup

APP = ['demo1.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
