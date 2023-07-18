import numpy as np


class OnnxInfer:


    def __init__(self):
        """
        Initialze hardware configurations
        """
        pass

    def load_network(self, model_path: str, device="cpu"):
        """
        load model from defined path
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
    def predict(self, image):
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
    model.load_network()
    img = (...)
    predictions = model.predict(image=img)
    model.visualize(predictions=predictions)