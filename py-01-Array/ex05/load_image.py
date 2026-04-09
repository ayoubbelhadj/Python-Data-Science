import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:
    """Load a JPG/JPEG image and return its pixels as an RGB ndarray."""
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("only JPG and JPEG formats are supported")

    try:
        with Image.open(path) as img:
            if img.format not in ("JPEG", "JPG"):
                raise ValueError("file is not a real JPEG image")
            img = img.convert("RGB")
            arr = np.array(img)
    except FileNotFoundError:
        raise FileNotFoundError(f"file not found: {path}")
    except UnidentifiedImageError:
        raise ValueError(f"cannot identify image file: {path}")

    print(f"The shape of image is: {arr.shape}")
    return arr
