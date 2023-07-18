from nerf.nn.modules import NeRF
from nerf.utils.metric import validation_metric


class Validator:
    """
    Class to validate model
    """

    def __init__(self, model_path):
        """
        Load model here
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
