from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """Load animal.jpeg, slice a 400x400 grayscale region, and display it."""
    try:
        arr = ft_load("animal.jpeg")
        print(arr)
        zoom = arr[100:500, 450:850, 0:1]
        print(f"New shape after slicing: {zoom.shape}")
        print(zoom)

        plt.imshow(zoom, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == '__main__':
    main()
