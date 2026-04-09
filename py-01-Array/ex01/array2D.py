import numpy as np


def _is_number(v) -> bool:
    """Return True if v is int or float but not bool."""
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D array and return a row-sliced version."""
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if len(family) == 0:
        raise ValueError("family must not be empty")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D array")
    row_len = len(family[0])
    if row_len == 0:
        raise ValueError("rows must not be empty")
    if not all(len(row) == row_len for row in family):
        raise ValueError("all rows must be the same size")
    if not all(_is_number(v) for row in family for v in row):
        raise TypeError("all values must be int or float")
    if not isinstance(start, int) or isinstance(start, bool):
        raise TypeError("start must be an int")
    if not isinstance(end, int) or isinstance(end, bool):
        raise TypeError("end must be an int")

    arr = np.array(family)
    new_arr = arr[start:end]

    print(f"My shape is : {arr.shape}")
    print(f"My new shape is : {new_arr.shape}")

    return new_arr.tolist()
