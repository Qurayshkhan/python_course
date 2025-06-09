class Employee:
    language = "python" # this is a class attribute
    salary= 12000

hassan = Employee()
hassan.name = "Hassan khan" # this is a instance attribute
print(hassan.name, hassan.language, hassan.salary)

husnain = Employee()
husnain.name = "Husnain khan"

print(husnain.name, husnain.language, husnain.salary)