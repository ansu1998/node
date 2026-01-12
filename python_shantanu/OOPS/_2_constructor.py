


#basic constructor
class Employee:
    empcnt = 0

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)

    def display_2(self):
        print(self.age)
        

obj = Employee('ansu',23)
print(obj.empcnt)
obj.display()
obj.display_2()



# class   Employee:
#     empcnt = 0

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        

#     def display(self):
#         print('Welcome %s...'%self.name)

#     def display_age(self):
#         print('your age is %d'%self.age)

# obj1 = Employee('sam',40)
# obj1.display()
# obj1.display_age()


'''
Lets create another class Rectangle .
A constructor is used to initialize the object values. Member function area() compute the area of the rectangle
'''

class Mobile:
    def set_details(self):
        self.company=input("enter compnay name...")
        self.model=input("enter model name..")
        self.price=input("enter price..")
    def display_details(self):
        print("Company Name=",self.company)
        print("Model=",self.model)
        print("Price=",self.price)
M=Mobile()
M.set_details()
M.display_details()


























