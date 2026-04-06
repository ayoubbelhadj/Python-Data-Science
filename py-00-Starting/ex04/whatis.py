import sys


def main():
    """Check if the argument is odd or even and print the result."""
    argv = sys.argv[1:]
    if len(argv) > 1:
        print("AssertionError: more than one argument are provided")
        return
    if not argv:
        return
    if not argv[0].lstrip('-').isdigit():
        print("AssertionError: argument is not an integer")
        return
    if int(argv[0]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
