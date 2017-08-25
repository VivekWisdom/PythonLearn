#/usr/bin/python3


class Duck:
    def __init__(self, **kwargs):
        self._variables = kwargs   
        
    def quack(self):
        return 'Duck Quacks'
    def walk(self):
        return 'Duck Walks'
    @property
    def color(self):
        return self._variables['color']
    @color.setter
    def color(self, c):
        self._variables['color'] = c
    @color.deleter
    def color(self):
        del self._variables['color']

def main():
    donald = Duck(color = 'Blue', age = 23)
    print(donald.color)
    donald.color = 'Red'
    print(donald.color)
    del donald.color
    try:
        print(donald.color)
    except KeyError:
        print('Color has been Deleted')


if __name__ == '__main__':
    main()