#!/usr/bin/env python3
"""Shear function"""
import tensorflow as tf


def shear_image(image, intensity): 
    """Randomly shears an image:
        image is a 3D tf.Tensor containing the image to shear.
        intensity is the intensity with which the image should be sheared.
        Returns the sheared image."""
