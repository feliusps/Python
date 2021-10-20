
# Inheritance is a way to form new classes using classes that have already been defined. 

#create two  classes called Dog and aanimal 

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("I am a Animal")

    def eat(self):
        print("Eating")


class Dog(Animal): #inherit animal
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("I am a Dog")

    def bark(self):
        print("Woof!")