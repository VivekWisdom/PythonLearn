#!/usr/bin/python3
""" This module reads a file contents and prints on the console. """
def main():
    infile = open('lines.text', 'r')
    outfile = open('new.txt', 'w')

    for line in infile:
        print(line, file = outfile)

if __name__ == '__main__':
    main()