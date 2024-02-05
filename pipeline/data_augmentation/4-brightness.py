#!/usr/bin/env python3
"""Brightness function"""
import tensorflow as tf


def change_brightness(image, max_delta):
    """Randomly changes the brightness of an image:
        image is a 3D tf.Tensor containing the image to change,
        max_delta is the maximum amount the image should be brightened
            (or darkened).
        Returns the altered image."""
    bright_img = tf.image.random_brightness(
        image,
        max_delta=max_delta
    )

    return bright_img
