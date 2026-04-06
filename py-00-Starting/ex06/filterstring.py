from ft_filter import ft_filter
import sys


def main():
    """Filter words from a string by minimum length.

    Takes two command-line arguments:
        argv[0]: a string of space-separated words
        argv[1]: a numeric minimum length (integer)

    Prints the list of words whose length is strictly greater than the given
    number. Raises AssertionError if the argument count is wrong or the second
    argument is not numeric.
    """
    try:
        argv = sys.argv[1:]
        assert len(argv) == 2, "the arguments are bad"
        assert argv[1].isnumeric(), "the arguments are bad"
        text = argv[0].split()
        nbr = int(argv[1])
        print(list(ft_filter(lambda x: len(x) > nbr, text)))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
