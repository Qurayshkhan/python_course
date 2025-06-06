def sum(n):
    if(n == 0 or n == 1):
        return n;
    return sum(n-1)+n;

print(sum(5));