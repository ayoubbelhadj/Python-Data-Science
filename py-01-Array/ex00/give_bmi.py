import numpy as np


def _is_number(v) -> bool:
    """Return True if v is int or float but not bool."""
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Compute BMI from paired height (m) and weight (kg) lists."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("height and weight must be the same size")
    if len(height) == 0:
        raise ValueError("lists must not be empty")
    if not all(_is_number(v) for v in height):
        raise TypeError("height must contain only int or float values")
    if not all(_is_number(v) for v in weight):
        raise TypeError("weight must contain only int or float values")

    h_arr = np.array(height, dtype=float)
    w_arr = np.array(weight, dtype=float)

    if np.any(h_arr <= 0) or np.any(w_arr <= 0):
        raise ValueError("height and weight values must be strictly positive")

    return (w_arr / h_arr ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans: True where bmi value is above limit."""
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("limit must be an int")
    if not all(_is_number(v) for v in bmi):
        raise TypeError("bmi must contain only int or float values")

    return [v > limit for v in bmi]
