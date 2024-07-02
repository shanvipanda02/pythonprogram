purchase_amount = 150
membership_level = 'Gold'

if membership_level == 'Platinum':
    discount = 0.20
elif membership_level == 'Gold':
    discount = 0.15
elif membership_level == 'Silver':
    discount = 0.10
else:
    discount = 0.05

final_amount = purchase_amount * (1 - discount)
print(f"Final amount after discount: ${final_amount:.2f}")

