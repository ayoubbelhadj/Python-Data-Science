def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a closure that applies function to x, updating x each call."""
    def inner() -> float:
        """Applies function to x, updates x, and returns the result."""
        nonlocal x
        x = function(x)
        return x
    return inner
