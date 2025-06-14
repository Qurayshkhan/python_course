class Employee:
    company = "Microsoft"
    
    def show(self):
        print(f"This company of the employee is {self.company}")
class Programmer(Employee):
    company = "Google"
    
    def showLanguage(self):
        print(f"This company of the programmer is {self.company}")

programmer = Programmer()
programmer.showLanguage()
programmer.show()