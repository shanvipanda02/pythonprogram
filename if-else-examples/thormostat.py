current_temp = 72
desired_temp = 68
mode = "cooling"

if mode == "cooling":
    if current_temp > desired_temp:
        print("Turning on the AC")
    elif current_temp < desired_temp:
        print("Turning off the AC")
    else:
        print("AC is in idle mode")
elif mode == "heating":
    if current_temp < desired_temp:
        print("Turning on the heater")
    elif current_temp > desired_temp:
        print("Turning off the heater")
    else:
        print("Heater is in idle mode")
else:
    print("System is off")

