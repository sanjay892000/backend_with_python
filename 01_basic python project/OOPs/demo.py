#abstraction

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def sayHello(self):
        pass        #abstract method

class Demo(Greet):
    def sayHello(self):
        return "Hello"

obj = Demo()
print(obj.sayHello())
