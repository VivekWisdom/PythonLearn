#!/usr/bin/python3
'''
sample.py demonastrates the some important modules of Python 3
'''

import sys
import os
import urllib.request
import random
import datetime

def main():
    '''
    Main function for the Modules Code Sample
    '''
    # Sys Demo
    print('My Python version is {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    print(sys.path)
    print()
    #os package demo
    print(os.cpu_count())
    print(os.getenv('path'))
    print(os.getcwd())
    print(os.urandom(20))
    print()
    #URLLIB Demo
    page = urllib.request.urlopen('http://www.vivekwisdom.com')

    for line in page:
        print(str(line, encoding='utf-8'), end='')
    print()

    # Random Demo

    print(random.randint(1, 1000))
    new_list = list(range(25))
    print(new_list)
    random.shuffle(new_list)
    print(new_list)

    # Datetime demo
    now = datetime.datetime.now()
    print(now)

if __name__ == '__main__':
    main()
