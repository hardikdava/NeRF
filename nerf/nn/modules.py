import torch
import os
import torch.nn as nn
import torch.nn.functional as F

import numpy as np
from nerf.utils.file import read_yaml_file


class NeRF(nn.Module):

    def __init__(self, model_cfg):
        super(NeRF, self).__init__()

        file_path, ext = os.path.splitext(model_cfg)

        if ext == ".yaml":
            # Load from scratch
            cfg = read_yaml_file(model_cfg)
            self.model_depth = cfg.get("model_depth", 8)
            self.model_width = cfg.get("model_width", 256)
            self.input_channel = cfg.get("input_channel", 3)
            self.output_channel = cfg.get("output_channel", 4)
            self.activation = cfg.get("nn", nn.ReLU())  # Choose activation function here
            self._create_model()
            initialize_weights(self)
        elif ext in [".pth", ".pt"]:
            # Load from pretrained weights
            # read from existing model dict
            pass

    def _create_model(self):
        lin_1 = nn.Linear(self.input_channel, self.model_width)
        layers_stack = []
        layers_stack.append(lin_1)
        for _ in range(self.model_depth - 1):
            layers_stack.append(nn.Linear(self.model_width, self.model_width))

        self.pts_linears = nn.ModuleList(layers_stack)
        self.output_linear = nn.Linear(self.model_width, self.output_channel)

    def set_weights(self, model):
        csd = model.float().state_dict()  # checkpoint state_dict as FP32
        self.load_state_dict(csd, strict=False)  # load

    def get_weights(self):
        return [val.cpu().numpy() for _, val in self.model.state_dict().items()]

    def forward(self, x):
        input_pts, input_views = torch.split(x, [self.input_channel, self.input_channel], dim=-1)
        h = input_pts
        for i, l in enumerate(self.pts_linears):
            h = self.pts_linears[i](h)
            h = self.activation(h)

        outputs = self.output_linear(h)

        return outputs


def initialize_weights(model):
    for m in model.modules():
        t = type(m)
        if t in [nn.Hardswish, nn.LeakyReLU, nn.ReLU, nn.ReLU6, nn.SiLU]:
            m.inplace = True


if __name__ == "__main__":
    model = NeRF(model_cfg="../../configs/model.yaml")
    device = torch.device('cpu')
    model = model.to(device)

