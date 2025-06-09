from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def booking(self, fro, to):
        print(f"Ticket booked of the train number: {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running of this time.")
    def getFare(self, fro, to):
        print(f"Ticket fare is train no {self.trainNo} from {fro} to {to} is {randint(222, 5555)}.")

t = Train(345345)
t.booking("Lahore", "Karachi")
t.getStatus()
t.getFare("Lahore", "Karachi")