#!/usr/bin/env python3
"""Crop function"""

def crop_image(image, size):
    """Performs a random crop of an image:
        image is a 3D tf.Tensor containing the image to crop.
        size is a tuple containing the size of the crop.
        Returns the cropped image."""
