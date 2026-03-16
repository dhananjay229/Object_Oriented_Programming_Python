class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def animal_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)