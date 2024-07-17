import time

# Initial setup for parking system
parking_lot = {
    "total_spots": 100,
    "available_spots": 100,
    "occupied_spots": 0,
    "vehicles": {},  # Dictionary to store vehicle information
    "rates": {
        "Car": 10,   # rate per hour
        "Bike": 5,   # rate per hour
        "Truck": 15  # rate per hour
    }
}

# Function to get the current timestamp
def current_time():
    return time.time()

# Function to park a vehicle
def park_vehicle(vehicle_number, vehicle_type):
    if parking_lot["available_spots"] > 0:
        if vehicle_number not in parking_lot["vehicles"]:
            if vehicle_type in parking_lot["rates"]:
                parking_lot["vehicles"][vehicle_number] = {
                    "type": vehicle_type,
                    "entry_time": current_time()
                }
                parking_lot["available_spots"] -= 1
                parking_lot["occupied_spots"] += 1
                return f"Vehicle {vehicle_number} parked successfully."
            else:
                return f"Unknown vehicle type: {vehicle_type}. Allowed types are: {', '.join(parking_lot['rates'].keys())}."
        else:
            return f"Vehicle {vehicle_number} is already parked."
    else:
        return "No available spots to park the vehicle."

# Function to calculate parking fee
def calculate_fee(entry_time, vehicle_type):
    parked_duration = (current_time() - entry_time) / 3600  # convert seconds to hours
    rate_per_hour = parking_lot["rates"][vehicle_type]
    return round(parked_duration * rate_per_hour, 2)

# Function to remove a parked vehicle
def remove_vehicle(vehicle_number):
    if vehicle_number in parking_lot["vehicles"]:
        vehicle_info = parking_lot["vehicles"][vehicle_number]
        fee = calculate_fee(vehicle_info["entry_time"], vehicle_info["type"])
        del parking_lot["vehicles"][vehicle_number]
        parking_lot["available_spots"] += 1
        parking_lot["occupied_spots"] -= 1
        return f"Vehicle {vehicle_number} removed successfully. Parking fee: ${fee}"
    else:
        return f"Vehicle {vehicle_number} not found in the parking lot."

# Function to display parking lot status
def parking_status():
    status = f"""
    Total Spots: {parking_lot['total_spots']}
    Available Spots: {parking_lot['available_spots']}
    Occupied Spots: {parking_lot['occupied_spots']}
    Vehicles Parked: {list(parking_lot['vehicles'].keys())}
    """
    return status.strip()

# Function to handle parking system operations
def parking_system():
    while True:
        print("\nParking System Menu:")
        print("1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. Parking Status")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            vehicle_type = input("Enter vehicle type (Car/Bike/Truck): ")
            result = park_vehicle(vehicle_number, vehicle_type)
            print(result)
        elif choice == "2":
            vehicle_number = input("Enter vehicle number to remove: ")
            result = remove_vehicle(vehicle_number)
            print(result)
        elif choice == "3":
            print(parking_status())
        elif choice == "4":
            print("Exiting Parking System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Start the parking system
parking_system()

