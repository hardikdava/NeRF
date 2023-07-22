"""
Export model in different model for inference accleration
"""

from nerf.nn.ner_model import NeRF


class Exporter:
    def __init__(self, model_path: str):
        self.model = NeRF(model_cfg=model_path)

    def export_onnx(self, **kwargs):
        """
        Export engine as onnx
        """
        pass

    def tensorflow_saved_model(self):
        pass

    def tensorrt_engine(self):
        pass

    def openvino_xml(self):
        pass
