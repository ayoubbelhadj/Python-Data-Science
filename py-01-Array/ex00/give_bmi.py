import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")
    if not all(isinstance(v, (int, float)) for v in height):
        raise TypeError("height must contain only int or float values")
    if not all(isinstance(v, (int, float)) for v in weight):
        raise TypeError("weight must contain only int or float values")
    if len(height) != len(weight):
        raise ValueError("height and weight lists must be the same size")

    h_arr = np.array(height, dtype=float)
    w_arr = np.array(weight, dtype=float)

    if np.any(h_arr <= 0):
        raise ValueError("height values must be strictly positive")
    if np.any(w_arr <= 0):
        raise ValueError("weight values must be strictly positive")

    return list(w_arr / h_arr ** 2)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    if not isinstance(limit, int):
        raise TypeError("limit must be an int")
    if not all(isinstance(v, (int, float)) for v in bmi):
        raise TypeError("bmi must contain only int or float values")

    return [v > limit for v in bmi]
