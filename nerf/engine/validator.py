from nerf.nn.ner_model import NeRF
from nerf.utils.metric import validation_metric


class Validator:
    """
    Class to validate engine
    """

    def __init__(self, model_path):
        """
        Load engine here
        """
        pass

    def get_dataloader(self):
        pass

    def val(self, dataset_path: str):
        """
        Predict on each image
        Computer error metric b/w gt and prediction
        """
        pass

    def plot(self):
        """
        Plot validation results
        """
