class Demo:
    a=5 # class attribute

o = Demo()
o.a=10 # instance attribute
print(o.a)

print(Demo().a)

# Does it change the class attribute
# No