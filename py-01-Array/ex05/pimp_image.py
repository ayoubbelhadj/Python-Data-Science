import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    invert = array.copy()
    invert = 255 - invert
    return invert


def ft_red(array) -> np.ndarray:
    """Keeps only the red channel."""
    red = array.copy()
    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0
    return red


def ft_green(array) -> np.ndarray:
    """Keeps only the green channel."""
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    return green


def ft_blue(array) -> np.ndarray:
    """Keeps only the blue channel."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    return blue


def ft_grey(array) -> np.ndarray:
    """Converts the image to grayscale."""
    grey = array.copy()
    g = grey.sum(axis=2) / 3
    grey[:, :, 0] = g
    grey[:, :, 1] = g
    grey[:, :, 2] = g
    return grey
