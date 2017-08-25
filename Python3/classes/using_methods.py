#/usr/bin/python3

class Duck:
    def __init__(self, value):
        self._v = value
    def quack(self):
        print('Quack', self._v)
    def walk(self):
        print('Walk', self._v)

def main():
    donald = Duck(34)
    donald.quack()
    donald.walk()

    frank = Duck(14)
    frank.quack()
    frank.walk()

if __name__ == '__main__':
    main()



