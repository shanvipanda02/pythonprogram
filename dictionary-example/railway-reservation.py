# Railway Reservation System Example with User Input

# Global dictionary to store train details
trains = {
    "12345": {"name": "Express", "seats": 50, "fare": 1000},
    "67890": {"name": "Local", "seats": 100, "fare": 500}
}

# Dictionary to store passenger reservations
reservations = {}

# Function to display available trains
def display_trains():
    print("\nAvailable Trains:")
    for train_id, details in trains.items():
        print(f"Train ID: {train_id}, Name: {details['name']}, Seats Available: {details['seats']}, Fare: {details['fare']}")

# Function to check seat availability
def check_availability(train_id, num_seats):
    if train_id in trains and trains[train_id]["seats"] >= num_seats:
        return True
    else:
        return False

# Function to book seats
def book_ticket(train_id, num_seats, passenger_name):
    if train_id in trains and trains[train_id]["seats"] >= num_seats:
        if train_id not in reservations:
            reservations[train_id] = {}
        if passenger_name in reservations[train_id]:
            print(f"Ticket booking failed. {passenger_name} already has a reservation.")
            return False
        reservations[train_id][passenger_name] = num_seats
        trains[train_id]["seats"] -= num_seats
        print(f"Ticket booked successfully for {passenger_name} on Train {train_id}. Seats Booked: {num_seats}")
        return True
    else:
        print("Ticket booking failed. Insufficient seats available.")
        return False

# Function to cancel reservation
def cancel_ticket(train_id, passenger_name):
    if train_id in reservations and passenger_name in reservations[train_id]:
        num_seats = reservations[train_id][passenger_name]
        del reservations[train_id][passenger_name]
        trains[train_id]["seats"] += num_seats
        print(f"Reservation cancelled successfully for {passenger_name}. Seats Released: {num_seats}")
        return True
    else:
        print("Cancellation failed. No such reservation found.")
        return False

# Main program execution
if __name__ == "__main__":
    while True:
        print("\n===== Railway Reservation System =====")
        print("1. Display Available Trains")
        print("2. Book Ticket")
        print("3. Cancel Reservation")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            display_trains()
        elif choice == "2":
            train_id = input("Enter Train ID: ")
            num_seats = int(input("Enter Number of Seats to Book: "))
            passenger_name = input("Enter Passenger Name: ")
            if check_availability(train_id, num_seats):
                book_ticket(train_id, num_seats, passenger_name)
        elif choice == "3":
            train_id = input("Enter Train ID: ")
            passenger_name = input("Enter Passenger Name: ")
            cancel_ticket(train_id, passenger_name)
        elif choice == "4":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

