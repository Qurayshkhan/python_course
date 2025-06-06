def c_to_f(f):
    return 5*(f-32)/9;

n = int(input("Enter a number in F: "))
print(f"{round(c_to_f(n), 2)} C");