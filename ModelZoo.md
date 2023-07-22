# Model Zoo:

| Model Name | Architecture | Weights | logs|
|--|--|--|--|
|[NeRF]() | [model.yaml](...) | [nerf.pt](...) |  |
|[InstantNGP]() | [instant-ngp.yaml](...) | [instant-ngp.pt](...) |  |
|[F2Nerf]() | [model.yaml](...) | [nerf.pt](...) |  |


## How to add new model:


1. Create new_model.yaml and add your model layers with activation function 
2. Add non-included model operations in `nerf/nn/modules/common.py`
3. Add hyperparameter configuration
4. Train and validate model
	

