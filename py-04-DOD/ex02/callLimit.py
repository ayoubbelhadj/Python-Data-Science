def callLimit(limit: int):
    """Limit the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Take the function to wrap."""
        def limit_function(*args: any, **kwds: any):
            """Call function only if limit not reached."""
            nonlocal count
            count += 1
            if (count > limit):
                print(f"Error: {function} call too many times")
            else:
                function(*args, **kwds)
        return limit_function
    return callLimiter
