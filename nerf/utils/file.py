import glob
import json
from pathlib import Path
from typing import Optional, Union, List
import yaml
import numpy as np


def read_yaml_file(file_path: str) -> dict:
    """
    Read a yaml file and return a dict.

    Args:
        file_path (str): The path to the yaml file.

    Returns:
        dict: A dict of content information
    """
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def save_yaml_file(data: dict, file_path: str) -> None:
    """
    Save a dict to a json file.

    Args:
        indent:
        data (dict): dict with unique keys and value as pair.
        file_path (str): The path to the json file.
    """

    with open(file_path, "w") as outfile:
        yaml.dump(data, outfile, sort_keys=False, default_flow_style=None)


def list_files_with_extensions(
    directory: Union[str, Path], extensions: Optional[List[str]] = None
) -> List[Path]:
    """
    List files in a directory with specified extensions or all files if no extensions are provided.

    Args:
        directory (Union[str, Path]): The directory path as a string or Path object.
        extensions (Optional[List[str]]): A list of file extensions to filter. Default is None, which lists all files.

    Returns:
        (List[Path]): A list of Path objects for the matching files.
    """
    directory = Path(directory)
    files_with_extensions = []

    if extensions is not None:
        for ext in extensions:
            files_with_extensions.extend(directory.glob(f"*.{ext}"))
    else:
        files_with_extensions.extend(directory.glob("*"))

    return files_with_extensions


def read_json_file(file_path: str) -> dict:
    """
    Read a json file and return a dict.

    Args:
        file_path (str): The path to the json file.

    Returns:
        dict: A dict of annotations information
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_json_file(data: dict, file_path: str, indent: int = 3) -> None:
    """
    Write a dict to a json file.

    Args:
        indent:
        data (dict): dict with unique keys and value as pair.
        file_path (str): The path to the json file.
    """
    with open(file_path, "w") as fp:
        json.dump(data, fp, indent=indent)
