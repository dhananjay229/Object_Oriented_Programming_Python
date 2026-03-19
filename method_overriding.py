class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def speak(self):
        print("Dog barking")

dog = Dog()
dog.speak()