import setuptools
from setuptools import find_packages
import re
import os
import subprocess

with open("./nerf/__init__.py", 'r') as f:
    content = f.read()
    version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("./requirements.txt", "r") as f:
    reqs = f.read().splitlines()


setuptools.setup(
    name="nerf",
    version=version,
    author="-----",
    author_email="-----",
    description="Nerf is framework to train Nerf models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="-----",
    install_requires=reqs,
    packages=find_packages(exclude=("tests",), include=("vision",)),
    extras_require={
        "dev": ["flake8", "black==22.3.0", "isort", "twine", "pytest", "wheel"],
    },
    entry_points={
        "console_scripts": [
            "nerf=nerf.nerf:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)