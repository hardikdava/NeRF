import setuptools
from setuptools import find_packages
import re
import os
import subprocess
from pathlib import Path


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("./requirements.txt", "r") as f:
    reqs = f.read().splitlines()


FILE = Path(__file__).resolve()
PARENT = FILE.parent  # root directory

print(PARENT)
README = (PARENT / "README.md").read_text(encoding="utf-8")

def get_version():
    file = PARENT / 'nerf/__init__.py'
    return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', file.read_text(encoding="utf-8"), re.M)[1]

setuptools.setup(
    name='nerf',
    version=get_version(),
    author='...',
    author_email='...',
    license='MIT',
    description=long_description,
    long_description=README,
    long_description_content_type='text/markdown',
    url='...',
    install_requires=reqs,
    packages=find_packages(),
    extras_require={
        'dev': [
            'flake8',
            'black==22.3.0',
            'isort',
            'twine',
            'pytest',
            'wheel',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        'Typing :: Typed',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS'
    ],
    keywords="machine-learning, deep-learning, NeRF",
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "nerf=nerf.nerf:main",
        ],
    },
)
