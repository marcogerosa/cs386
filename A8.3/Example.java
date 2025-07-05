// Base class
abstract class Animal {
    public abstract String makeSound();
}

// Subclasses
class Dog extends Animal {
    @Override
    public String makeSound() {
        return "Woof!";
    }
}

class Cat extends Animal {
    @Override
    public String makeSound() {
        return "Meow!";
    }
}

class Bird extends Animal {
    @Override
    public String makeSound() {
        return "Tweet!";
    }
}

// Client code using polymorphism
public class PolymorphismExample {
    // Method that accepts any Animal object
    public static void printAnimalSound(Animal animal) {
        System.out.println(animal.makeSound());
    }
    
    public static void main(String[] args) {
        // Creating objects of different subclasses
        Animal dog = new Dog();
        Animal cat = new Cat();
        Animal bird = new Bird();
        
        // Same method works with different object types
        printAnimalSound(dog);   // Output: Woof!
        printAnimalSound(cat);   // Output: Meow!
        printAnimalSound(bird);  // Output: Tweet!
        
        // Polymorphism in an array of different Animal types.
        Animal[] animals = {new Dog(), new Cat(), new Bird()};
        
        for (Animal animal : animals) {
            // The same command is sent to each animal, which will implement it differently
            printAnimalSound(animal); 
        }
    }
}
