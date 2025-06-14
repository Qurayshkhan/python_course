class Employee:
    def __init__(self):
        print("Employee Constructor.")
    a = 1
class Programmer(Employee):
    def __init__(self):
       print("Programmer Constructor.")
    b = 2    
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Manager constructor")
    c = 5

# o = Employee()
o = Manager()
print(o.a)
print(o.b)
print(o.c)
