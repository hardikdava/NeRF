import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

class NeRF:


    def __init__(self, model_depth, model_width, input_channel, output_channel):
        super(self).__init__()
        self.model_depth = model_depth
        self.model_width = model_width
        self.input_channel = input_channel
        self.output_channel = output_channel

    def set_weights(self):
        pass

    def get_weights(self):
        pass

    def forward(self):
        pass