class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

dog = Dog()
dog.speak()
dog.bark()
