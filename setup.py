from distutils.core import setup
from setuptools import setup

setup(
    name="subtodl", 
    packages = ['Scripts'], 
    version="0.0.1",
    license='MIT',     
    description = 'a handy tools to download subtitle ',   
    author = 'mehdi',                  
    author_email = 'gudarzi.gi@gmail.com',  
    install_requires=[
    "pyqt5; platform_system=='Windows'", 
    "beautifulsoup4", 
    "lxml",
    "PyQt5 ;platform_system=='Linux'",
    "requests",
    "wget",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
    entry_points={

        'gui_scripts': [
        'subtodl= Scripts.subtodlmain:main',
    ],
    },
    data_files=[
    ('/share/applications/', ["subtodl.desktop"]
     )
    ]

)
