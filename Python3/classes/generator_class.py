#/usr/bin/python3

class RangeModified:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: 
            raise TypeError('Requires at least one argument')
        elif numargs == 1:
            self._start = 0
            self._step = 1
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
            self._step = 1
        elif numargs == 3:
            if args[2] < 1:
                self._start = args[0]
                self._stop = args[1]
                self._step = 1
            else:
                (self._start, self._stop, self._step) = args
        else: 
            raise TypeError('Needs at max 3 arguments')

    def __iter__(self):
        i = self._start
        while i <= self._stop:
            yield i
            i+=self._step

def main():
    for i in RangeModified(5, 25, 2):
        print(i, end=' ')

if __name__ == '__main__':
    main()