class A:
    def disp_a(self):
        print("Display Function From Class A")

class B:
    def disp_b(self):
        print("Display Function From Class B")

class C(A,B):
    def disp_c(self):
        print("Display Function From Class C")

a = A()
a.disp_a()

b= B()
b.disp_b()

c= C()
c.disp_c()
c.disp_a()
c.disp_b()

