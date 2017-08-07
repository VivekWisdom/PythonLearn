""" This module reads a file contents and prints on the console. """
#!usr/bin/python

FH = open('lines.text')

for line in FH.readlines():
    print(line, end='')
