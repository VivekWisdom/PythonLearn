#!/usr/bin/python3
""" Module for Exception Code Sample """

try:
    FH = open('line1s.text')

    for line in FH.readlines():
        print(line)
except IOError as e:
    print('File Not Found !! ({})'.format(e))
