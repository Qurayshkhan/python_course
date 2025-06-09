with open("file.txt") as f:
    text = f.read();
    if("Twinkle" in text):
        print("Twinkle is present in text.");
    else:
         print("Twinkle is not present in text.");