from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def main():
    """Test all 5 image filters and display the results."""
    try:
        array = ft_load("landscape.jpg")
        print(array)

        fig, axes = plt.subplots(2, 3, figsize=(12, 8))
        axes[0, 0].imshow(array)
        axes[0, 0].set_title("Original")
        axes[0, 1].imshow(ft_invert(array))
        axes[0, 1].set_title("Invert")
        axes[0, 2].imshow(ft_red(array))
        axes[0, 2].set_title("Red")
        axes[1, 0].imshow(ft_green(array))
        axes[1, 0].set_title("Green")
        axes[1, 1].imshow(ft_blue(array))
        axes[1, 1].set_title("Blue")
        axes[1, 2].imshow(ft_grey(array), cmap="gray")
        axes[1, 2].set_title("Grey")
        plt.show()

        print(ft_invert.__doc__)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
    