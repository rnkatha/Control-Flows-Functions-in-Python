def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting the user for input
original_price = float(input("6000: "))
discount_percentage = float(input("25: "))

# Calculating the final price
final_price = calculate_discount(original_price, discount_percentage)

# Printing the final price
if final_price != original_price:
    print("Final price after discount:", final_price)
else:
    print("No discount applied. Original price:", original_price)
