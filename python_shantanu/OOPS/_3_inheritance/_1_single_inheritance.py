
'''
Inheritance is the capability of one class to derive or inherit the properties from another class. 
The class that derives properties is called the derived class or child class and the class from which
the properties are being derived is called the base class or parent class.

'''


class A:
    a = 123
    def disp_a(self):
        print('Display Function From class A')
class B(A):
    b = 456
    def disp_b(self):
        print('Display Function From class B')

obj1 = A()
obj2 = B()
# A
print(obj1.a)
obj1.disp_a()

# B
print(obj2.b)
obj2.disp_b()

# # B(A)
print(obj2.a)
obj2.disp_a()
 

