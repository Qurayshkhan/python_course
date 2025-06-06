mark1 = int(input("Enter a mark 1: "));
mark2 = int(input("Enter a mark 2: "));
mark3 = int(input("Enter a mark 3: "));

totalPercentage = ((mark1+mark2+mark3)*100)/300;

if(totalPercentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
    print("You are passed with: ", totalPercentage);
else:
    print("You are failed.");