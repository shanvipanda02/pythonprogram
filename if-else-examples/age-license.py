age = 19 
is_citizen = True 
criminal_record = True

if age >= 18 and is_citizen and not criminal_record:
    print("You are eligible to vote.")
elif age < 18:
    print("You are too young to vote.")
elif not is_citizen:
    print("You must be a citizen to vote.")
elif criminal_record:
    print("You cannot vote due to your criminal record.")

