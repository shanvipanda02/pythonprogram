# Real Estate Management System Example with User Input

# Global dictionary to store property details
properties = {
    "1": {"name": "Apartment A", "type": "Apartment", "price": 150000, "availability": True},
    "2": {"name": "House B", "type": "House", "price": 250000, "availability": False},
    "3": {"name": "Villa C", "type": "Villa", "price": 500000, "availability": True}
}

# Dictionary to store bookings
bookings = {}

# Function to display available properties
def display_properties():
    print("\nAvailable Properties:")
    for prop_id, details in properties.items():
        status = "Available" if details["availability"] else "Booked"
        print(f"Property ID: {prop_id}, Name: {details['name']}, Type: {details['type']}, Price: ${details['price']}, Status: {status}")

# Function to check property availability
def check_availability(prop_id):
    if prop_id in properties and properties[prop_id]["availability"]:
        return True
    else:
        return False

# Function to book property
def book_property(prop_id, customer_name):
    if prop_id in properties and properties[prop_id]["availability"]:
        properties[prop_id]["availability"] = False
        bookings[prop_id] = {"customer_name": customer_name}
        print(f"Property '{properties[prop_id]['name']}' booked successfully by {customer_name}.")
        return True
    else:
        print("Property booking failed. Property not available.")
        return False

# Function to cancel property booking
def cancel_booking(prop_id):
    if prop_id in properties and not properties[prop_id]["availability"]:
        customer_name = bookings[prop_id]["customer_name"]
        properties[prop_id]["availability"] = True
        del bookings[prop_id]
        print(f"Booking cancelled successfully for Property ID {prop_id}. Property now available.")
        return True
    else:
        print("Cancellation failed. No booking found for the given Property ID.")
        return False

# Main program execution
if __name__ == "__main__":
    while True:
        print("\n===== Real Estate Management System =====")
        print("1. Display Available Properties")
        print("2. Book Property")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            display_properties()
        elif choice == "2":
            prop_id = input("Enter Property ID to Book: ")
            customer_name = input("Enter Customer Name: ")
            if check_availability(prop_id):
                book_property(prop_id, customer_name)
        elif choice == "3":
            prop_id = input("Enter Property ID to Cancel Booking: ")
            cancel_booking(prop_id)
        elif choice == "4":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

