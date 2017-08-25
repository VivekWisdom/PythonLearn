#/usr/bin/python3

class Animal:
    def talk(self):
        return 'Animal Talks'
    def walk(self):
        return 'Animal Walks'
    def clothes(self):
        return 'Animal have nice cloths'

class Duck(Animal):
    def __init__(self, **kwargs):
        self._variables = kwargs   
    def set_variables(self, k, v):
        self._variables[k] = v
    def get_variables(self, k):
        return self._variables.get(k, None)

    def quack(self):
        return 'Duck Quacks'
    def walk(self):
        super().walk()
        return 'Duck Walks'
class Dog(Animal):
    def clothes(self):
        return 'I have fur'

def main():
    donald = Duck(color = 'Blue', age = 23)

    print(donald.quack())
    print(donald.walk())
    print(donald.clothes())

    print(donald.get_variables('color'))
    print(donald.get_variables('age'))
    print(donald.get_variables('anything'))

    fido = Dog()
    print(fido.clothes())

if __name__ == '__main__':
    main()