
# Decorators in Python are a design pattern that allows you to add new
# functionality to an existing object without modifying its structure. They
# are commonly used to extend the behavior of functions or methods.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


# context manager
class manger():
    def __init__(self, filename,mode):
        self.filename =filename
        self.mode = mode

    def  __enter__(self):
        self.file1 = open(self.filename,self.mode)
        return self.file1

    def __exit__(self, exc_type, exc_value, traceback):
        self.file1.close()

with manger('test.txt', 'w') as f:
    f.write("hiii...its me")        


