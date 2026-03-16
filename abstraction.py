from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starting")

    def stop(self):
        print("Car stopping")

class Bike(Vehicle):
    def start(self):
        print("Bike starting")

    def stop(self):
        print("Bike stopping")

car = Car()
bike = Bike()

car.start()
car.stop()
bike.start()
bike.stop()