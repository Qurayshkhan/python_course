with open("file.txt") as f:
    content1 = f.read()
    
with open("my-file.txt") as f:
    content2 = f.read()
if(content1 == content2):
    print("Yes both file content are identical.")
else:
    print("No both file content are not identical.")

    