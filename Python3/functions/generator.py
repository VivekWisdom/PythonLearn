#/usr/bin/python3

def main():
    for i in inclusive_range(4, 25, 2,):
        print(i, end=' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('Requires at least one argument')
    elif numargs == 1:
        start = 0
        step = 1
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('Needs at max 3 arguments')

    i = start
    while i <= stop:
        yield i
        i +=step

if __name__ == "__main__":
    main()