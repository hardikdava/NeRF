
class Predictor:

    def __init__(self, model_path: str):
        pass

    def __call__(self, *args, **kwargs):
        """
        Predict depends on model type
        e.g. load pytorch, onnx or other formats
        """
        pass

    def predict(self):
        """
        Useful for batch prediction
        """