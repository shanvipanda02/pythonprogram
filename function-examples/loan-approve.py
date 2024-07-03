age = 30
income = 50000
credit_score = 700

if age >= 18:
    if income >= 40000:
        if credit_score >= 650:
            print("Loan approved")
        else:
            print("Loan denied due to low credit score")
    else:
        print("Loan denied due to insufficient income")
else:
    print("Loan denied due to age")
