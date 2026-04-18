def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Print descriptive statistics for the given data.

    Args:
        *args: Numeric values to compute statistics on.
        **kwargs: Named statistics to compute. Each value must be one of:
                  "mean", "median", "quartile", "var", "std".
                  Prints "ERROR" for each requested stat if no data
                  is provided.
    """
    for key, stat in kwargs.items():
        if len(args) == 0:
            print("ERROR")
        elif stat == "mean":
            mean = sum(args) / len(args)
            print(f"mean : {mean}")
        elif stat == "median":
            s = sorted(args)
            n = len(s)
            if n % 2 == 1:
                median = s[n // 2]
            else:
                median = (s[n // 2 - 1] + s[n // 2]) / 2
            print(f"median : {median}")
        elif stat == "quartile":
            s = sorted(args)
            n = len(s)
            q1 = s[n // 4]
            q3 = s[(3 * n) // 4]
            quartile = [float(q1), float(q3)]
            print(f"quartile : {quartile}")
        elif stat == "var":
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            print(f"var : {variance}")
        elif stat == "std":
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            std = variance ** 0.5
            print(f"std : {std}")
