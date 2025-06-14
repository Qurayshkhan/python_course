class Employee:
    a = 1;    
    
    @classmethod
    def show(self):
        print(f"it is a class methods. {self.a}.");

o = Employee()
o.a  = 45;
o.show()
