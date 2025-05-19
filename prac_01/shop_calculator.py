# Shop calculator program
items_bought = int(input("Number of items: "))
while items_bought < 0:
    print("Invalid number of items!")
    items_bought = int(input("Number of items: "))

total_price = 0
for i in range(items_bought):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

print(f"Total price for {items_bought} items is ${total_price:.2f}")
