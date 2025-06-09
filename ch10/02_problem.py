class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"Square root of the square is: {self.n * self.n}")
    def cube(self):
        print(f"Cube of the number is: {self.n * self.n * self.n}")
    def sqRoot(self):
        print(f"Square root of the number is: {self.n **1/2}")
number = Calculator(4)
number.square()
number.cube()
number.sqRoot()