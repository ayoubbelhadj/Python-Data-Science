from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_transpose(arr):
    """Transpose a 2D array by swapping rows and columns."""
    h, w = arr.squeeze().shape
    result = np.zeros((w, h), dtype=arr.dtype)
    for i in range(h):
        for j in range(w):
            result[j, i] = arr[i, j]
    return result


def main():
    """Load animal.jpeg, crop, transpose manually, and display."""
    try:
        arr = ft_load("animal.jpeg")
        zoom = arr[100:500, 450:850, 0:1]
        print(f"The shape of image is: {zoom.shape}")
        print(zoom)

        rotate = ft_transpose(zoom)
        print(f"New shape after Transpose: {rotate.shape}")
        print(rotate)

        plt.imshow(rotate, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == '__main__':
    main()
