light_color = "green"
pedestrian_crossing = False

if light_color == "green":
    if pedestrian_crossing:
        print("Wait for pedestrians to cross")
    else:
        print("Go")
elif light_color == "yellow":
    if pedestrian_crossing:
        print("Prepare to stop and wait for pedestrians")
    else:
        print("Prepare to stop")
elif light_color == "red":
    print("Stop")
else:
    print("Invalid light color")

