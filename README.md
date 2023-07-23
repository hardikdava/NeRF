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
pip install git+https://github.com/hardikdava/NeRF.git
```

or for development

```bash
pip install -e ".[dev]"
```


### Usage:

**Command line usage:**
```bash
nerf mode=predict model= "" video="" output="" resolution=800

nerf mode=train model= "" data="" output="" resolution=800

nerf mode=val model= "" data="" output="" resolution=800

nerf mode=export model= "" output="" fp16=True resolution=800 format=onnx
```

**Python usage:**
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
- Generate camera poses from video sequence. This will also extract frames as per given argument.



## Deployment:

Please visit [deployment guideline](https://github.com/hardikdava/NeRF-Exp/blob/main/DEPLOYMENT.md) for integrating models into production.


## Project Structure:

```bash
.
├── configs
│   ├── default.yaml  # Default settings here
│   └── hyps.yaml  # hypermeter configurations
├── data  # Dataset Configurations File
│   └── lego.yaml
├── DEPLOYMENT.md
├── examples
│   └── onnx_infer.py  # ONNX-Runtime example API for non-trainable models
├── experiments # Experiments logs directory for experiment management
├── LICENSE
├── nerf
│   ├── dataset 
│   │   ├── data_loader.py
│   │   └── __init__.py
│   ├── engine  
│   │   ├── exporter.py
│   │   ├── __init__.py
│   │   ├── predictor.py
│   │   ├── trainer.py
│   │   └── validator.py
│   ├── __init__.py
│   ├── models  # Add new models here
│   │   ├── instant-nerf.yaml
│   │   └── nerf.yaml
│   ├── nerf.py  # Entry point for usage
│   ├── nn  # All machine learning functions here
│   │   ├── __init__.py
│   │   ├── loss.py  # Loss functions 
│   │   ├── modules
│   │   │   └── common.py  
│   │   └── nerf_model.py  # model creation and weights loading, scalable for quantization
│   └── utils
│       ├── colmap_utils.py  # functions from colmap
│       ├── file.py
│       ├── __init__.py
│       ├── logger.py  # Add new loggers here e.g. clearml, wandb, neptune, etc
│       ├── metric.py  # Evaluation metrics
│       ├── torch_utils.py 
│       └── visualizer.py  # Different visualizer e.g. blender, Open3D, Opencv etc
├── README.md
├── requirements.txt   
├── scripts
│   └── download_example_data.sh  # Data download scripts
├── setup.py 
├── test
│   └── hello_test.py # Tests files
└── tools
    ├── generate_mesh.py # from depth images to mesh file
    └── images_to_pose_colmap.py # from video frames to camera pose
```

## Model File:

```
model_depth: d
model_width: w
resolution: r
activation: nn.ReLU()
quantize_aware_training: False
density_head:
	-[[mlp, [previous_node, next_node],[in, out, pad, stride]],
		[mlp, [previous_node, next_node],[in, out, pad, stride]],
		[mlp, [previous_node, next_node],[in, out, pad, stride]],
		[mlp, [previous_node, next_node],[in, out, pad, stride]],
		[mlp, [previous_node, next_node],[in, out, pad, stride]],
		[mlp, [previous_node, next_node],[in, out, pad, stride]],
		[mlp, [previous_node, next_node],[in, out, pad, stride]],
		[mlp, [previous_node, next_node],[in, out, pad, stride]]]
color_head:
	-[[mlp, [previous_node, next_node],[in, out, pad, stride]],
model:
	- [density_head, color_head]

```

## LICENSE:

## Citations:
