# NeRF (Neural Radiance Fields)
A template repo holding our common setup for a python project.


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
