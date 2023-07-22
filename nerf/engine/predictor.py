"""
Prediction from trained model
"""

from nerf.nn.ner_model import NeRF
from nerf.utils.colmap_utils import preprocess_video

class Predictor:
    def __init__(self, model_path: str):
        pass

    def __call__(self, *args, **kwargs):
        """
        Predict depends on engine type
        e.g. load pytorch, onnx or other formats
        """
        pass

    def predict(self):
        """
        Useful for batch prediction
        """
        preprocess_video()

    def annotate(self):
        """
        Plot labels if needed
        """

    def generate_mesh(self):
        pass
