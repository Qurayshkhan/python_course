with open("old.txt") as f:
    content = f.read()

with open("rename_file_python.txt", "w") as f:
    f.write(content)