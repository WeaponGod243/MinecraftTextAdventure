import os
from distutils.core import setup
import py2exe


setup(
    console=[
        {
            "script": "main.py",
            "icon_resources": [(1, "favicon.ico")]
        }
    ],
    name="MCText Adventure"
)
