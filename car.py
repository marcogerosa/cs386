class Car:
    def turn_on(self):
        print("Turning on a car.")

class Audi(Car):
    def turn_on(self):
        print("Turning on an Audi.")

class Driver:
    def drive(self, c: Car):
        c.turn_on()
