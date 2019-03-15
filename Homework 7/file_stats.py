"""Homework 7 for CSE-41273"""
# Greg Seda
import sys


def stats(file_name):
    with open(file_name) as file:
        contents = file.read()
        characters = len(contents)
        words = len(contents.split())
        lines = len(contents.splitlines())
        line = contents.split("\n")
        longest = 0
        for l in line:
            if len(l) > longest:
                longest = len(l)

    return characters, words, lines, longest


if __name__ == "__main__":
    file_name = sys.argv[1]
    c, w, l, ll = stats(file_name)
    print("Characters: {}".format(c))
    print("Words: {}".format(w))
    print("Lines: {}".format(l))
    print("Longest line: {}".format(ll))
