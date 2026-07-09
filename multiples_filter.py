# Step 1: Generate a list of numbers from 1 to 20
numbers = list(range(1, 21))  
multiples_of_three = []

# Step 2: Loop through each number
for num in numbers:
    # Step 3: Check if the remainder of division by 3 is exactly 0
    if num % 3 == 0:
        multiples_of_three.append(num)

# Step 4: Print the result
print("Numbers divisible by 3:", multiples_of_three)