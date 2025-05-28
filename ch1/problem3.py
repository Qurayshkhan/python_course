import os;

directlyPath = '/';

contents = os.listdir(directlyPath);

for item in contents:
    print(item);