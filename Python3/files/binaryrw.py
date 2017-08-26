#!/usr/bin/python3
""" This module reads/write a binary file contents and prints on the console. """
def main():
    buffersize = 50000
    infile = open('sample.jpeg', 'rb')
    outfile = open('newsample.jpeg', 'wb')
    buffer = infile.read(buffersize)
    
    while len(buffer):
        outfile.write(buffer)
        print('.', end='')
        buffer = infile.read(buffersize)
    print()
    print('Read and Write Done.')

if __name__ == '__main__':
    main()