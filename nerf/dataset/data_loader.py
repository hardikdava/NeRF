import cv2
import numpy as np
from torch.utils.data import DataLoader, Dataset, dataloader, distributed

from nerf.utils.file import list_files_with_extensions

IMG_FORMATS = ["png", "jpg", "jpeg", "JPG"]


class InfiniteDataLoader(dataloader.DataLoader):
    """Dataloader that reuses workers

    Uses same syntax as vanilla DataLoader
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        object.__setattr__(self, "batch_sampler", _RepeatSampler(self.batch_sampler))
        self.iterator = super().__iter__()

    def __len__(self):
        return len(self.batch_sampler.sampler)

    def __iter__(self):
        for _ in range(len(self)):
            yield next(self.iterator)


class _RepeatSampler:
    """Sampler that repeats forever

    Args:
        sampler (Sampler)
    """

    def __init__(self, sampler):
        self.sampler = sampler

    def __iter__(self):
        while True:
            yield from iter(self.sampler)


def create_dataloader(**kwargs):
    dataset = LoadDataset(**kwargs)
    loader = DataLoader
    return loader(dataset, None, None, None), dataset


class LoadDataset:
    def __init__(self, **kwargs):
        """
        Initialize Dataset based on different type e.g. blender, liff, etc
        """
        pass

    def __len__(self):
        """
        return total number of data in instance
        """
        return

    def __getitem__(self, index):
        """
        iterator over dataset
        """
        return
