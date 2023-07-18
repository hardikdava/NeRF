import os
import sys
from typing import Dict, List

MODES = ["train", "predict", "export"]

CLI_HELP_MSG = f"""
    Arguments received: {str(['nerf'] + sys.argv[1:])}. 'nerf' commands use the following syntax:

        nerf MODE ARGS

        Where   MODE (required) is one of {MODES}
                ARGS (optional) are any number of custom 'arg=value' pairs like 'imgsz=320' that override defaults.

    1. Train a detection model for 10 epochs with an initial learning_rate of 0.01
        vision train data=train_cfg.yaml model="model.yaml" epochs=10 lr0=0.01
    """


def extract_info(args: List[str], key: str, split="="):
    for arg in args:
        arg_splitted = arg.split(split)
        if arg_splitted[0] == key:
            return arg_splitted[1]
    print("unknown command found")


def find_help(args) -> bool:
    for arg in args:
        arg_splitted = arg.split("--")
        print(arg_splitted)


def main(debug="") -> None:
    args = (debug.split(" ") if debug else sys.argv)[1:]
    if not args:  # no arguments passed
        print(CLI_HELP_MSG)
        return
    elif find_help(args):
        print("Help command found")
    mode = extract_info(args, key="mode")

    # DO TRAIN, VALID, PREDICT, EXPORT from here based on command
