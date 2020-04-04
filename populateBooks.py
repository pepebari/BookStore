#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import urllib.request

url = "https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books.csv"
urllib.request.urlretrieve(url, "books.csv")

with open('books.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            print(f'\ttitle: {row[0]} author: {row[1]} catId: {row[2]}')
        line_count += 1
    print(f'Processed {line_count} lines.')

