import nibabel as nib
import numpy as np


class BrainMap:
    """Represent a brain map object
    """

    def __init__(self, brain_map_object):
        """
        Initialize from a brain map object that was loaded from the nii files. 
        """
        self.brain_structure_name = brain_map_object.brain_structure
        self.data_indices = range(
            brain_map_object.index_offset,
            brain_map_object.index_offset + brain_map_object.index_count)
        if brain_map_object.vertex_indices is not None:
            self.surface_indices = brain_map_object.vertex_indices._indices
        else:
            self.surface_indices = []


def load_nii_brain_data_from_file(nii_path):
    """
    Convert nii object into matlab matrix, and brain model meta data
    :param nii_path: A path to a nii file
    :return: numpy matrix containing the image data, brain models iterable
    """
    nib_data = nib.load(nii_path)
    return np.array(nib_data.dataobj), [BrainMap(i) for i in nib_data.header.matrix.get_index_map(1).brain_models]


def load_nii_brain_image_from_file(nii_path):
    res, _ = load_nii_brain_data_from_file(nii_path)
    return res

def save_image_to_file(image, nii_path):
    nib.save(image, nii_path)
