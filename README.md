# NeRF (Neural Radiance Fields)

This repository is an implementation of NeRF based on pytorch. It has capability of easy to integrate other models as well.  Some of the key features are as following.

 - Easy installation for developers 
 - Easy deployment using onnx-runtime (No framework needed, depends on model) 
 - Integrate other models based on core modules.
 - Export models to various format e.g. onnx, openvino, tensorrt,
   coreml, etc.
 - Experiment management


## Download Sample Data:

```bash
sh ./scripts/download_example_data.sh
```

## Installation

You can install the package using pip

```bash
pip install git+https://github.com/hardikdava/NeRF-Exp.git
```

or for development

```bash
pip install -e ".[dev]"
```


### Usage:

Command line usage:
```bash
nerf mode=predict model= "" video="" output="" resolution=800

nerf mode=train model= "" data="" output="" resolution=800

nerf mode=val model= "" data="" output="" resolution=800

nerf mode=export model= "" output="" fp16=True resolution=800 format=onnx
```

Python usage:
```python
from nerf import nerf
model = nerf(model="")
model.train(data="", resolution=800, output_dir="")
model.val(data="", resolution=800, output_dir="")
model.export(data="", resolution=800, output_dir="", format="onnx")
model.predict(data="", resolution=800, output_dir="")
```

## Tools:

If you have video sequence or sequence of frames from any camera source then prior to run `NeRF`, it is suggested to get camera poses between camera frames. It can be achieved by using colmap though it can be based on model type. Some model do not require camera poses.

- Download [colmap2nerf](https://github.com/NVlabs/instant-ngp/blob/master/scripts/colmap2nerf.py)
- Genrate camera poses from video sequence. This will also extract frames as per given argument.



## Deployment:

Please visit [deployment guideline](https://github.com/hardikdava/NeRF-Exp/blob/main/DEPLOYMENT.md) for integrating models into production.


