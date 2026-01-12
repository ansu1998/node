class A:
    a = 123
    def disp_a(self):
        print("Display Function From Class A")

class B(A):
    b = 456
    def disp_b(self):
        print("Display Function From Class B")

class C(B):
    c = 789

    def disp_c(self):
        print("Display Function From Class C")

class D(C):
    d = 321

    def disp_d(self):
        print("Display Function From Class D")

a = A()
print(a.a)
a.disp_a()

b=B()
print(b.b)
b.disp_b()
print(b.a)
b.disp_a()

c = C()
print(c.c)
c.disp_c()
print(c.b)
print(c.a)
c.disp_b()
c.disp_a()

d=D()
print(d.d)
d.disp_d()

print(d.a)
print(d.b)
print(d.c)

d.disp_a()
d.disp_b()
d.disp_c()













