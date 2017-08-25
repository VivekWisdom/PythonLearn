#/usr/bin/python3

class Duck:
    def __init__(self, **kwargs):
        self._variables = kwargs   
    def set_variables(self, k, v):
        self._variables[k] = v
    def get_variables(self, k):
        return self._variables.get(k, None)

    def quack(self):
        return 'Duck Quacks'
    def walk(self):
        return 'Duck Walks'

def main():
    donald = Duck(color = 'Blue', age = 23)
    donald.quack()
    donald.walk()

    print(donald.quack())
    print(donald.walk())

    print(donald.get_variables('color'))
    print(donald.get_variables('age'))
    print(donald.get_variables('anything'))

if __name__ == '__main__':
    main()