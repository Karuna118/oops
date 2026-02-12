from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("The animal is sleeping")

class dog(animal):
    def sound(self):
        print("Animal is barking")

class cat(animal):
    def sound(self):
        
        print("Animal is sounding Meow")

class cow(animal):
    def sound(self):
        print("Animal is sounding MOO")

d=dog()
c=cat()
co=cow()

d.sound()
c.sound()
co.sound()