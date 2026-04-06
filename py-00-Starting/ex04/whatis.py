import sys


def main():
    argv = sys.argv[1:]
    if len(argv) > 1:
        print("AssertionError: more than one argument is provided")
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


main()
