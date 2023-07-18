from torch.utils.data import DataLoader, Dataset, dataloader, distributed
import numpy as np
from nerf.utils.file import list_files_with_extensions

import cv2

IMG_FORMATS = ["png", "jpg", "jpeg", "JPG"]


class InfiniteDataLoader(dataloader.DataLoader):
    """ Dataloader that reuses workers

    Uses same syntax as vanilla DataLoader
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        object.__setattr__(self, 'batch_sampler', _RepeatSampler(self.batch_sampler))
        self.iterator = super().__iter__()

    def __len__(self):
        return len(self.batch_sampler.sampler)

    def __iter__(self):
        for _ in range(len(self)):
            yield next(self.iterator)


class _RepeatSampler:
    """ Sampler that repeats forever

    Args:
        sampler (Sampler)
    """

    def __init__(self, sampler):
        self.sampler = sampler

    def __iter__(self):
        while True:
            yield from iter(self.sampler)


class LoadDatset:

    def __init__(self, data_dir, input_shape=800):
        self.input_shape = input_shape
        image_list = list_files_with_extensions(directory=data_dir, extensions=IMG_FORMATS)
        self.images = [cv2.imread(image_path) for image_path in image_list]

    def get_data(self):
        return self.images, 

