import random


computer = random.choice([-1, 1, 0]);

userSelect = input("Select a one of these, water, gun, snake");

dict = {"s": 1, "w": -1, "g": 0};

userNumber = dict[userSelect];

if(computer == userNumber):
    print("Draw");
else:
    if(computer == -1 and userNumber == 1):
        print('You Win');
    elif(computer == -1 and userSelect == 0):
        print("You win");
    elif(computer == 1  and userNumber == -1):
        print("You win");
    elif(computer == 1 and userNumber == 0):
        print("You lose");
    elif(computer == 0 and userNumber == 1):
        print("You Win");
    else:
        print("something went wrong")