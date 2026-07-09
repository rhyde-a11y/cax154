# Ask the user for input and immediately convert the string to an integer
age = int(input("Enter your age: "))

# Decision tree based on the age provided
if age < 18:
    print("Access denied. Too young!")
elif age <= 20:  # This captures 18, 19, and 20
    print("You can come in, but no drinking! 🚫🍷")
else:            # This captures anything 21 or older
    print("Welcome in! Enjoy your night.✌︎︎")

if age >54:
    print("You are eligible for our senior discount! 🧓💰")