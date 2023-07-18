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
├── .github
│   └── workflows
│       └── test.yml # holds our github action config 
├── .gitignore
├── README.md
├── setup.py
├── src
│   ├── __init__.py 
│   ├── hello.py 
└── test 
    └── test_hello.py
```

### Tests 🧪

[`pytests`](https://docs.pytest.org/en/7.1.x/) is used to run our tests.

### Publish on PyPi 🚀

**Important**: Before publishing, edit `__version__` in [src/__init__](/src/__init__.py) to match the wanted new version.

You can publish by using

```
export PYPI_USERNAME="you_username"
export PYPI_PASSWORD="your_password"
export PYPI_TEST_PASSWORD="your_password_for_test_pypi"
make publish -e PYPI_USERNAME=$PYPI_USERNAME -e PYPI_PASSWORD=$PYPI_PASSWORD -e PYPI_TEST_PASSWORD=$PYPI_TEST_PASSWORD
```

You can also use token for auth, see [pypi doc](https://pypi.org/help/#apitoken). In that case,

```
export PYPI_USERNAME="__token__"
export PYPI_PASSWORD="your_token"
export PYPI_TEST_PASSWORD="your_token_for_test_pypi"
make publish -e PYPI_USERNAME=$PYPI_USERNAME -e PYPI_PASSWORD=$PYPI_PASSWORD -e PYPI_TEST_PASSWORD=$PYPI_TEST_PASSWORD
```

**Note**: We will try to push to [test pypi](https://test.pypi.org/) before pushing to pypi, to assert everything will work


## Why no cookiecutter?
This is a template repo, it's meant to be used inside GitHub upon repo creation.

## Why reinvent the wheel?

There are several very good templates on GitHub, I prefer to use code we wrote instead of blinding taking the most starred template and having features we don't need. From experience, it's better to keep it simple and general enough for our specific use cases.
