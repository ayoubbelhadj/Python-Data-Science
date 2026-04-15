class calculator:
    """Static vector calculator."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Compute and print the dot product of V1 and V2."""
        result = sum(V1[i] * V2[i] for i in range(len(V1)))
        print(f"Dot Product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Compute and print the element-wise addition of V1 and V2."""
        vec = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is : {vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Compute and print the element-wise subtraction of V2 from V1."""
        vec = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is : {vec}")
