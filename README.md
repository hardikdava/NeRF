# NeRF (Neural Radiance Fields)

This is a implementation of NeRF of [this](https://arxiv.org/pdf/2003.08934.pdf) paper.


## Download Sample Data:

```bash
sh ./scripts/download_example_data.sh
```

## Installation

You can install the package using pip

```bash
pip install -e .
```

or for development

```bash
pip install -e ".[dev]"
```

## Structure

The project has the following structure

```
├── .gitignore
├── README.md
├── setup.py
├── nerf
│   ├── __init__.py 
│   ├── trainer.py
│   ├── exporter.py
```
