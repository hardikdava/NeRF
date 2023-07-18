from nerf.nn.model import NeRF


class Exporter:

    def __init__(self, model_path: str):

        self.model = NeRF(model_cfg=model_path)

    def export_onnx(self, **kwargs):
        """
        Export model as onnx
        """
        pass

