from abc import ABC, abstractmethod

class A(ABC):
    def m1(self):
        print("A")
        self.m2()
        print("B")
        self.m3()
        print("C")
    
    @abstractmethod
    def m2(self):
        pass
    
    @abstractmethod
    def m3(self):
        pass

class B(A):
    def m2(self):
        print("A")
    
    def m3(self):
        print("B")

class C(A):
    def m2(self):
        print("B")
    
    def m3(self):
        print("A")

def m(a: A):
    a.m1()

if __name__ == "__main__":
    b = B()
    c = C()
    m(b)
    m(c)
