with open("log.txt") as f:
    content = f.read()

if("Lorem" in content):
    print("Lorem is present in content.")
else:
    print("Lorem is not present in content.")