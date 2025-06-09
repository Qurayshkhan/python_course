class Employee:
    language = "python"
    salary= 10000
    
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"This is {self.name} and i am {self.language} developer. my salary is {self.salary}.")

    @staticmethod    
    def greet():
        print("Good morning.")
    
hassan = Employee("Hassan khan", "Python", 20000)
print(hassan.name, hassan.language, hassan.salary)