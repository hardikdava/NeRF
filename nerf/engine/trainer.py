import argparse
from pathlib import Path
from typing import Union

import torch

from nerf.dataset.data_loader import create_dataloader
from nerf.nn.ner_model import NeRF
from nerf.utils.logger import Logger


class Trainer:
    def __init__(self, cfg="configs/default.yaml"):
        self.cfg = self._get_config()
        self.model = NeRF()
        self.logger = Logger()

    def _pretrain(self):
        """
        To save data for experiment management
        E.g. hyps, input args, data samples for verification
        """
        pass

    def _get_config(self):
        """
        Read yaml/json files where configuration is saved
        """
        pass

    def get_dataloaders(self, dataset_type: str):
        data_loader = None
        if dataset_type == "train":
            data_loader, dataset = create_dataloader()  # Train Path
        elif dataset_type == "val":
            data_loader, dataset = create_dataloader()  # Val Path
        return data_loader

    def train(self):
        # Data loader
        # Model attributes
        # LRScheduler
        # Loss Function definition
        # Early Stopping fn
        # Optimizer
        # Most important: Continuous metric logging
        model = self.get_model(self.args.model)
        train_loader = self.get_dataloader(self.args.trainset)
        optimizer = self.build_optimizer(self.args.optimizer, self.hyps)

        for epoch in self.cfg.epochs:
            for data, label in train_loader:
                loss = self.criterion(model(data), label)  # forward pass
                loss.backward()  # backward pass
                optimizer.step()
                self.logger.info(loss)

            self.save_model()  # Trigger engine saving fn
        self.model.eval()
        self.valid()  # Validate engine after training for final accuracy

    def load_model(self, model_weights):
        """
        Load engine:
        option-1: From scratch and initialize random weights
        option-2: From pretrained weights for finetuning purpose
        """
        self.model = NeRF(model_weights)  # Initialize engine

    def build_optimizer(self):
        """
        Build Optimizer based on hyp selection
        Options: Adam, SGD, etc
        """
        pass

    def save_model(self):
        """
        Define strategy for saving engine mechanism
        E.g. Every engine, every nth engine or best/last engine
        """
        pass


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cfg", type=str, default="", help="engine.yaml path")
    parser.add_argument(
        "--device", default="", help="cuda device, i.e. 0 or 0,1,2,3 or cpu"
    )

    return parser.parse_args()


if __name__ == "__main__":
    pass
