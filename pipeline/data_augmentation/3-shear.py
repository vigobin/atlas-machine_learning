#!/usr/bin/env python3
"""Shear function"""
import tensorflow as tf


def shear_image(image, intensity):
    """Randomly shears an image:
        image is a 3D tf.Tensor containing the image to shear.
        intensity is the intensity with which the image should be sheared.
        Returns the sheared image."""
    return tf.keras.preprocessing.image.random_shear(image,
                                                     intensity,
                                                     row_axis=1,
                                                     col_axis=0,
                                                     channel_axis=2,
                                                     )
