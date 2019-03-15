"""Homework 7 for CSE-41273"""
# Greg Seda
import sys


def re_order(in_file, out_file):
    with open(in_file, 'r') as current_file:
        lines = current_file.read().split('\n')
        while '' in lines:
            lines.remove('')
    new_file = open(out_file, 'w')
    for line in lines:
        columns = line.split(',')
        columns[1], columns[0] = columns[0], columns[1]
        writer = str(",".join(columns)) + "\n"
        new_file.write(writer)
    new_file.close()


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    re_order(in_file, out_file)
