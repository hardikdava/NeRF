# NeRF (Neural Radiance Fields)

This repository is an implementation of NeRF based on pytorch. It has capability of easy to integrate other models as well.  Some of the key features are as following.

 - Easy installation for developers 
 - Easy deployment using onnx-runtime (No framework needed) 
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

## Tools:

If you have video sequence or sequence of frames from any camera source then prior to run `NeRF`, it is mandatory to get camera poses between camera frames. It can be achieved by using colmap.

- Download [colmap2nerf](https://github.com/NVlabs/instant-ngp/blob/master/scripts/colmap2nerf.py)
- Genrate camera poses from video sequence. This will also extract frames as per given argument.



## Deployment:

Please visit [deployment guideline](https://github.com/hardikdava/NeRF-Exp/blob/main/DEPLOYMENT.md) for integrating models into production.

