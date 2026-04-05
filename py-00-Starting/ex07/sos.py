import sys

def main():
    """Convert a command-line string argument to Morse code and print it.

    Expects exactly one argument containing only alphanumeric characters and spaces.
    Each character is looked up in NESTED_MORSE and the results are joined with spaces.
    Raises AssertionError if the argument count or content is invalid.
    """
    try:
        argv = sys.argv[1:]
        assert len(argv) == 1 , "the arguments are bad"
        assert all(c.isalnum() or c.isspace() for c in argv[0]), "the arguments are bad"
        
        NESTED_MORSE = {
            ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
            'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        }
        text = []
        for c in argv[0]:
            assert c.upper() in NESTED_MORSE, "the arguments are bad"
            text.append(NESTED_MORSE.get(c.upper()))
        print(' '.join(text))
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()