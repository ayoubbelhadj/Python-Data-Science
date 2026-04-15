class calculator:
    """
    Vector calculator that applies scalar operations
    to all elements of a list.
    """

    def __init__(self, v):
        """Initialize with a copy of list v."""
        self.vec = v[:]

    def __add__(self, object) -> None:
        """Add scalar to all elements."""
        self.vec = [n + object for n in self.vec]
        print(self.vec)

    def __mul__(self, object) -> None:
        """Multiply all elements by scalar."""
        self.vec = [n * object for n in self.vec]
        print(self.vec)

    def __sub__(self, object) -> None:
        """Subtract scalar from all elements."""
        self.vec = [n - object for n in self.vec]
        print(self.vec)

    def __truediv__(self, object) -> None:
        """Divide all elements by scalar. Prints error on division by zero."""
        if object == 0:
            print("Error: division by zero")
            return
        self.vec = [n / object for n in self.vec]
        print(self.vec)
