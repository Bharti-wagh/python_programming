#CAN YOU CHANGE THE SELF PARAMETER INSIDE A CLASS TO SOMETHING ELSE (SAY "BHARTI").TRY CHNAGING SELF TO SELF 
# "SLF" OR "BHARTI" AND SEE THE EFFECTS.
class Train:
    def __init__(bharti, name, fare, seats):
        bharti.name = name
        bharti.fare = fare
        bharti.seats = seats

    def get_status(bharti):
        print(f"Train Name: {bharti.name}")
        print(f"Seats Available: {bharti.seats}")

    def fare_info(bharti):
        print(f"Ticket Price: ₹{bharti.fare}")

    def book_ticket(bharti):
        if bharti.seats > 0:
            print(f"Your ticket has been booked! Seat number: {bharti.seats}")
            bharti.seats -= 1
        else:
            print("Sorry, train is full! No seats available.")

# Example usage:
train1 = Train("Rajdhani Express", 1500, 3)

train1.get_status()
train1.fare_info()

train1.book_ticket()
train1.book_ticket()
train1.get_status()
