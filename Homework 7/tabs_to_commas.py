"""Homework 7 for CSE-41273"""
# Greg Seda
import csv
import string
import sys


def tab_to_comma(in_file, out_file):
    with open(in_file) as file:
        csv_reader = csv.reader(file, delimiter='\t')
        with open(out_file, 'wt') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
            for row in csv_reader:
                csv_writer.writerow(row)

if __name__ == "__main__":
    in_file = sys.argv[1]
    tab_to_comma(in_file, 'colors_commas.csv')
