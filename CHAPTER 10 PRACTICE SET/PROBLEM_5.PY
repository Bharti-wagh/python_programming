#WRITE A CLASS TRAIN WHICH HAS METHOD TO BOOK A TICKET , GET STATUS(NO OF SEATS) AND 
# GET FARE INFORMATION OF TRAIN RUNNING UNDER INDIAN RAILWAYS.
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"Train Name: {self.name}")
        print(f"Seats Available: {self.seats}")

    def fare_info(self):
        print(f"Ticket Price: ₹{self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Seat number: {self.seats}")
            self.seats -= 1
        else:
            print("Sorry, train is full! No seats available.")
            
train1 = Train("Rajdhani Express", 1500, 5)

train1.get_status()
train1.fare_info()

train1.book_ticket()
train1.book_ticket()

train1.get_status()
