#!/usr/bin/python3
""" This module reads a file contents and prints on the console. """

FH = open('lines.text')

for line in FH.readlines():
    print(line)
