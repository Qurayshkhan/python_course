def rem(l, word):
    n = [];
    for item in l:
        n.append(item.strip(word))
    return n;

l = ["Hassan", "Husnain", "Elephant", "Hussain"];

print(rem(l, "an"));