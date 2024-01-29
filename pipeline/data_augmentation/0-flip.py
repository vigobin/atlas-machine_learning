#!/usr/bin/env python3
"""Flip function"""
import tensorflow as tf


def flip_image(image):
    """Flips an image horizontally:
        image is a 3D tf.Tensor containing the image to flip.
        Returns the flipped image."""
    flipped = tf.image.flip_left_right(image)
    return flipped
