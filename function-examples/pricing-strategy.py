customer_type = "VIP"
total_purchase = 200

if customer_type == "VIP":
    if total_purchase > 500:
        discount = 0.30
    elif total_purchase > 300:
        discount = 0.20
    else:
        discount = 0.10
elif customer_type == "Regular":
    if total_purchase > 500:
        discount = 0.15
    elif total_purchase > 300:
        discount = 0.10
    else:
        discount = 0.05
else:
    discount = 0.02

final_price = total_purchase * (1 - discount)
print(f"Final price: ${final_price:.2f}")
