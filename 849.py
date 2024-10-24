from abc import ABC, abstractmethod

class B(ABC):
    @abstractmethod
    def act(self):
        pass

class B1(B):
    def act(self):
        print("A")

class B2(B):
    def act(self):
        print("B")

class A:
    def __init__(self):
        self.b = None
    
    def change_b(self, b: B):
        self.b = b
    
    def do_something(self):
        self.b.act()

# This replaces the Java Main class and main method
if __name__ == "__main__":
    a = A()
    b1 = B1()
    b2 = B2()
    
    a.change_b(b2)
    a.do_something()  # Prints: B
    
    a.change_b(b1)
    a.do_something()  # Prints: A
