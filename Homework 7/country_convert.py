"""Homework 7 for CSE-41273"""
# Greg Seda

import csv
from operator import itemgetter


in_file = open('countryInfo.csv', 'r')
reader = csv.DictReader(in_file, delimiter='\t')
list_of_countries = []

for row in reader:
    country_dict = {'Country': row['name'], 'capital': row['capital'],
                    'population': int(row['population'])}
    list_of_countries.append(country_dict)

in_file.close()

sorted_list = sorted(list_of_countries, key=itemgetter('population'),
                     reverse=True)

out_file = open('country_simple_info.csv', 'w')
fieldnames = ['Country', 'capital', 'population']

writer = csv.DictWriter(out_file, fieldnames=fieldnames)
writer.writeheader()

for item in sorted_list:
    writer.writerow(item)

out_file.close()
