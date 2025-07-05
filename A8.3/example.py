# Base class
class Animal:
    def make_sound(self):
        pass

# Subclasses
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Client code using polymorphism
def animal_sound(animal):  # Accepts any Animal object
    return animal.make_sound()

# Usage - same function works with different object types
dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
