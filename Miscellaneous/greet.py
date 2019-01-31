import sys
import argparse

DEFAULT_TEXT = "World"
DEFAULT_GREETING = "Hello"


def greet(text=DEFAULT_TEXT, greeting=DEFAULT_GREETING):
    """ Prints 'Hello World' (default) or 'Hello {text}' """
    if not text:
        text = DEFAULT_TEXT
    if not greeting:
        greeting = DEFAULT_GREETING
    print("{} {}".format(greeting, text))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text', nargs='?', help="text to output after Hello")
    parser.add_argument(
        '-g', '--gretting',
        help="string for getting in place of 'Hello'"
    )
    arguments = parser.parse_args()
    greet(arguments.text, arguments.greeting)
