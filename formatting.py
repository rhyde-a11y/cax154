#In Python, `f` before a string denotes an **f-string** (short for **Formatted String Literal**).

#Introduced in Python 3.6, f-strings are the modern, cleanest, and fastest way to insert variables or expressions directly inside a string.


### How It Works
#You just put an `f` or `F` right before your opening quotation mark, and then you can wrap any Python variable or expression in curly braces `{}`. Python will evaluate whatever is inside those braces and convert it into text.

name = "Alice"
age = 25

# The old way (concatenation)
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

# The modern way (f-string)
print(f"Hello, my name is {name} and I am {age} years old.")
# Output: Hello, my name is Alice and I am 25 years old.

### Neat Tricks You Can Do with f-Strings
#f-strings aren't just for variables; you can run code right inside the curly braces.

#### 1. Math and Expressions

#You can do math operations or call functions directly inside the braces:

print(f"Next year, I will be {age + 1} years old.")
# Output: Next year, I will be 26 years old.

print(f"My name in uppercase is {name.upper()}.")
# Output: My name in uppercase is ALICE.

#### 2. Inline Debugging (The `=` shortcut)

#If you are debugging code and want to print both the variable name *and* its value, add an `=` sign inside the braces:

x = 10
y = 25

print(f"{x=}, {y=}")
# Output: x=10, y=25

#### 3. Formatting Numbers (Decimals & Percentages)

#You can control how numbers look by adding a colon `:` followed by formatting rules:

pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
# Output: Pi rounded to 2 decimal places: 3.14

percentage = 0.756
print(f"Success rate: {percentage:.1%}")
# Output: Success rate: 75.6%
