from random import randint
class Train:
    def __init__(this, trainNo):
        this.trainNo = trainNo
    def booking(this, fro, to):
        print(f"Ticket booked of the train number: {this.trainNo} from {fro} to {to}")
    def getStatus(this):
        print(f"Train no: {this.trainNo} is running of this time.")
    def getFare(this, fro, to):
        print(f"Ticket fare is train no {this.trainNo} from {fro} to {to} is {randint(222, 5555)}.")

t = Train(345345)
t.booking("Lahore", "Karachi")
t.getStatus()
t.getFare("Lahore", "Karachi")