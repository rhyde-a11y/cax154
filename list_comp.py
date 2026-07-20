# # List Comprehension (creates the entire list in memory)
# my_list = [x * 2 for x in range(10)]

# # Generator Expression (creates an on-demand iterator)
# my_gen = (x * 2 for x in range(10))

# print(my_gen) # Convert generator to list for printing
# print(my_list)  # Print the list created by list comprehension

import sys
import time

def double_and_log(x):
    print(f"   -> Processing {x}...")
    return x * 2

print("--- 1. CREATING THE LIST COMPREHENSION ---")
# This will execute the function for all 5 items immediately.
my_list = [double_and_log(x) for x in range(5)]
print("List comprehension created!\n")

print("--- 2. CREATING THE GENERATOR EXPRESSION ---")
# This will set up the generator, but NOT run the function yet.
my_gen = (double_and_log(x) for x in range(5))
print("Generator expression created! (Notice how nothing printed above)\n")

print("--- 3. CONSUMING THE GENERATOR ---")
# The work happens only now, on-demand, as we loop through it.
for value in my_gen:
    print(f"Received value: {value}")