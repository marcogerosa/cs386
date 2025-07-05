class Car {
   void turnOn() {
       System.out.println("Turning on a car.");
   }
}


class Audi extends Car {
   void turnOn() {
       System.out.println("Turning on an Audi.");
   }
}


class Driver {
   void drive(Car c) {
       c.turnOn();
   }
}
