class Employee:
    a = 1;    
    
    @classmethod
    def show(self):
        print(f"it is a class methods. {self.a}.");
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0];
        self.lname = value.split(" ")[1]; 
         

o = Employee()
o.a = 45;
o.name  = "Hassan khan";
o.show()
print(o.name)
