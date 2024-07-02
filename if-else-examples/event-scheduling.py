day_of_week = "Saturday"
time_of_day = "afternoon"

if day_of_week in ["Saturday", "Sunday"]:
    if time_of_day == "morning":
        print("Morning Yoga Class")
    elif time_of_day == "afternoon":
        print("Afternoon Dance Class")
    else:
        print("Evening Meditation Class")
else:
    if time_of_day == "morning":
        print("Morning Run Club")
    elif time_of_day == "afternoon":
        print("Afternoon Painting Workshop")
    else:
        print("Evening Language Class")

