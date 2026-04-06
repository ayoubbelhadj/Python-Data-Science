import sys


def main():
    """Counts character types in a string."""
    argv = sys.argv[1:]
    assert len(argv) <= 1, "more than one argument is provided"
    if len(argv) == 1:
        text = argv[0]
    else:
        text = input("What is the text to count?\n") + "\n"
    upper = lower = digit = space = punctuation = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        else:
            punctuation += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except (EOFError, KeyboardInterrupt):
        print("No data provided to input function")
