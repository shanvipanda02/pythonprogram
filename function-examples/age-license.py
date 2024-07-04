def agelicence(age,is_citizen,criminal_record):
    if age >= 18 and is_citizen and not criminal_record:
        print("You are eligible to vote.")
    elif age < 18:
        print("You are too young to vote.")
    elif not is_citizen:
        print("You must be a citizen to vote.")
    elif criminal_record:
        print("You cannot vote due to your criminal record.")
age = 19 # mb1
is_citizen = False #mb2
criminal_record = False # mb3
agelicence(age,is_citizen,criminal_record)

