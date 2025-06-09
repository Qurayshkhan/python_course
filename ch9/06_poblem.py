with open("log.txt") as f:
    lines = f.readlines()

lineNo = 1

for line in lines:
    if("python" in line):
        print(f"Yes python is present in line: {lineNo}")
        break
    else:
        print("Python is not present")
    lineNo += 1
else:
    print("No Lines found.")