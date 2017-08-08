#!/usr/bin/python3
""" Using polymorphism and complex OOP consepts in Python """

class AnimalActions(object):
    """ Base class AnimalActions to e shared across classes. """
    def quack(self):
        """ In the forest method """
        return self.strings['quack']
    def feathers(self):
        """ In the forest method """
        return self.strings['feathers']
    def bark(self):
        """ In the forest method """
        return self.strings['bark']
    def fur(self):
        """ In the forest method """
        return self.strings['fur']

class Duck(AnimalActions):
    """ Class Duck to define properties of Duck """
    strings = dict(
        quack="Quaaaaak!",
        feathers="The duck has gray and white feathers.",
        bark="The duck cannot bark.",
        fur="The duck has no fur."
    )
 
class Person(AnimalActions):
    """ Class Person to define properties of Person """
    strings = dict(
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
    )

class Dog(AnimalActions):
    """ Class Dog to define properties of Dog """
    strings = dict(
        quack="The dog cannot quack.",
        feathers="The dog has no feathers.",
        bark="Arf!",
        fur="The dog has white fur with black spots."
    )

def in_the_doghouse(dog):
    """ In the doghouse  method """
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    """ In the forest method """
    print(duck.quack())
    print(duck.feathers())

def main():
    """ main method for the module """
    donald = Duck()
    john = Person()
    fido = Dog()

    print("- In the forest:")
    for obj in (donald, john, fido):
        in_the_forest(obj)

    print("- In the doghouse:")
    for obj in (donald, john, fido):
        in_the_doghouse(obj)
if __name__ == "__main__":
    main()
