import glob

import numpy as np
from typing import Tuple


def preprocess_video(video_path: str, output_dir: str) -> str:
    """
    Extract poses from video sequence and store frames using colmap
    """


def read_data(data_dir) -> Tuple[np.ndarray, np.ndarray]:
    """
    Read images from directory
    Read pose from json file
    """
    img, poses = [], []
    return img, poses


class OnnxInfer:


    def __init__(self):
        """
        Initialze hardware configurations
        """
        pass

    def load_network(self, model_path: str, device="cpu"):
        """
        load engine from defined path
        """
        pass

    def _preprocess(self, image):
        """
        preprocess images
        """
        pass

    def _infer(self, processed_image):
        """
        Only inference part here
        """
    def predict(self, data_dir):
        images, poses = read_data(data_dir)

        for image, pose in range(len(images)):
            processed_image = self._preprocess(image=image)
            predictions = self._infer(processed_image=processed_image)
            processed_predictions = self._postprocess(predictions)
        return processed_predictions

    def _postprocess(self, predictions: np.ndarray):
        """
        post process predictions
        """
        pass

    def visualize(self, predictions: np.ndarray):
        """
        annotation/visualize predictions
        """
        pass


if __name__ == "__main__":

    model = OnnxInfer()


    video_path = "..."
    output_dir = model.preprocess_video(video_path)

    model.load_network()
    predictions = model.predict(output_dir=output_dir)
    model.visualize(predictions=predictions)