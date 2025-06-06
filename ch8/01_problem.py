def graterNumber(a, b, c):
    if(a > b and a > c):
        return a;
    elif(b > a and b > c):
        return b;
    elif(c > a and c > b):
        return c;
print(graterNumber(5,10,4));