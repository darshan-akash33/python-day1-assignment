# task2_yourname.py
total_bill = float(input("Enter total bill amount: ₹"))
num_people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))
tip_amount = (tip_percent / 100) * total_bill
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / num_people
tip_amount = round(tip_amount, 2)
total_with_tip = round(total_with_tip, 2)
amount_per_person = round(amount_per_person, 2)
print("\n--- Smart Bill Splitter ---")
print(f"Total Bill: ₹{total_bill}")
print(f"Tip Percentage: {tip_percent}%")
print(f"Tip Amount: ₹{tip_amount}")
print(f"Total with Tip: ₹{total_with_tip}")
print(f"Each Person Pays: ₹{amount_per_person}")

