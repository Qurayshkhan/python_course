class Employee:
    a = 1
class Programmer(Employee):
    b = 2    
class Manager(Programmer):
    c = 5

# o = Employee()
o = Manager()
print(o.a)
print(o.b)
print(o.c)
