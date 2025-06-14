class TwoDVector:
    def __init__(self, i, j):
        self.i = i;
        self.j = j;
    def show(self):
        print(f"This vector is 2D vector: {self.i}i {self.j}j");

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j);
        self.k = k;
        
    def show(self):
        print(f"This vector is 3D vector: {self.i}i {self.j}j {self.k}k");

a = TwoDVector(1,2);
a.show()
b = ThreeDVector(4,2,7);
b.show()