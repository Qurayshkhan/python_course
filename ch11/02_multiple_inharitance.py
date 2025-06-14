class Employee:
    company = "Microsoft"
    def show(self):
        print(f"This company of the employee is {self.company}.")
    
class Coder:
    language = "Python"
    
    def printLanguages(self):
        print(f"The language of the employee is: {self.language}.")
    
class Programmer(Employee, Coder):
    company = "Google"
    
    def showLanguage(self):
        print(f"This company of the programmer is {self.company}.")

programmer = Programmer()
programmer.showLanguage()
programmer.show()
programmer.printLanguages()