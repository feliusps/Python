
# implement polymorfhism using class cat and dog using secuential method, loop method,
# function method.


#create clsses
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Woof!' 
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow!' 
    
#method  secuemtial
# create instances
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

# method 2 using loop
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

#method 3 using function
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)