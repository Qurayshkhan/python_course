class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

hassan = Programmer("Hassan khan", 120000, 5400)
print(hassan.name, hassan.salary, hassan.pin, hassan.company)

ali = Programmer("Ali khan", 120000, 5400)
print(ali.name, ali.salary, ali.pin, ali.company)