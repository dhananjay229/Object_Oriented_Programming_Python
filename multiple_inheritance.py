class GrandFather:
    def house(self):
        print("GrandFather has a house")

class Father(GrandFather):
    def car(self):
        print("Father has a car G Wagon")

class Son(Father):
    def bike(self):
        print("Son has a bike BMW 301 R")

son = Son()
son.house()
son.car()
son.bike()
