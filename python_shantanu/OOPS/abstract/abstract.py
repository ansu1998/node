
#An abstract method is a method that has a declaration but does not have an implementation. 

from abc import  ABC, abstractmethod

class Shape(ABC):
    @abstractmethod

    def noofsides(self):
        self.a=123
        self.b=456

class Triangle(Shape):
    def noofsides(self):
        self.c=789
        print('3 sides')

class Pentagon(Shape):
    def noofsides(self):
        print('5 sides')


class Hexagon(Shape):
    def noofsides(self):
        print('6 sides')

# s=Shape()
# s.noofsides()

t=Triangle()
t.noofsides()
# print(t.a,t.b,t.c)
print(t.c)

p=Pentagon()
p.noofsides()

h=Hexagon()
h.noofsides()
