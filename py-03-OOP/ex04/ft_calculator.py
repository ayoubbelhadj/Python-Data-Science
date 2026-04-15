class calculator:
    """Static vector calculator."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Compute and print the dot product of V1 and V2."""
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Compute and print the element-wise addition of V1 and V2."""
        vec = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Compute and print the element-wise subtraction of V2 from V1."""
        vec = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {vec}")
