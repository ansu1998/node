'''

In programming, 
polymorphism means the same function name (but different signatures) being used for different types.

# len() being used for a string
print(len("geeks"))
 
# len() being used for a list
print(len([10, 20, 30]))

real world example


overloading

overriding
'''

'''
overriding

Method overriding in Python is when you have two methods with the same name that each perform different tasks. 
In other words, the child class has access to the properties and functions of the parent class method while also 
extending additional functions of its own to the method. 

If a method in a superclass coincides with that of a subclass,then the subclass is said to override the superclass.

'''



class A:
    def display(self):
        print("this is  class A")

    def display_4(self):
        print("Display_parent")

class B(A):
    def display(self):
        print("This is class A, overriding")

    def display_4(self):
        print("Display_parent Overriding")

    def display_b(self):
        print("This is class B")

b=B()
b.display()
b.display_b()
b.display_4()


'''
OVERLOADING-

The problem with method overloading in Python is that we may overload the methods 
but can only use the latest defined method. 

'''


def random(a,b=None,c=None):
    if b:
        return a*b
    if c:
        return a*c
    return a*2
    
print(random(5,c=7))

