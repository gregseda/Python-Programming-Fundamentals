"""Homework 7 for CSE-41273"""
# Greg Seda

import csv
import operator
import sys


def re_sort(in_file, out_file):
    data = csv.reader(open(in_file, newline=''), delimiter=',')
    header = next(data)
    sortedlist = sorted(data, key=operator.itemgetter(1))
    with open(out_file, "w", newline='') as csvfile:
        cvs_writer = csv.writer(csvfile, delimiter=',')
        cvs_writer.writerow(header)
        cvs_writer.writerows(sortedlist)


if __name__ == "__main__":
    in_file = sys.argv[1]
    re_sort(in_file, 'books_sort.csv')
