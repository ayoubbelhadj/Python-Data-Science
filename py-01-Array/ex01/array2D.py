import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family list have to be 2D Array")
    row_len = len(family[0])
    if not all(len(row) == row_len for row in family):
        raise ValueError("all rows must be the same size")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")

    arr = np.array(family)
    new_arr = arr[start:end]

    print(f"My shape is: {arr.shape}")
    print(f"My new shape is: {new_arr.shape}")

    return new_arr
