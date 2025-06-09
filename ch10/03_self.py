class Employee:
    language = "python"
    salary= 10000
    
    def getInfo(self):
        print(f"This is {self.name} and i am {self.language} developer. my salary is {self.salary}.")
       
    @staticmethod    
    def greet():
        print("Good morning.")
    
hassan = Employee()
hassan.name = "Hassan khan"
hassan.getInfo()
hassan.greet()