import os
from distutils.core import setup
import py2exe

setup(
    console=[
        {
            "script": "MCText.py",
            "icon_resources": [(1, "favicon.ico")]
        }
    ],
    zipfile=None,
    name="MCText Adventure"
)
