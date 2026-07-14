def calculate_price(original_price, discount_rate):
    original_price = float(input("Enter the original price: "))
    discount_rate = float(input("Enter the discount rate (as a decimal): "))
    discounted_price = original_price * (1 - discount_rate)
    return discounted_price

result = calculate_price(0,0)
print(f"The discounted price is: ${result:.2f}")