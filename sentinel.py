CORRECT_PASSWORD = "python123"
max_attempts = 3
attempts = 0

# The loop keeps running ONLY IF the wrong password is typed AND attempts are left
# We initialize 'guess' as an empty string so the loop can start
guess = ""

while guess != CORRECT_PASSWORD and attempts < max_attempts:
    guess = input("Enter password: ")
    
    if guess != CORRECT_PASSWORD:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Incorrect! Attempts remaining: {remaining}")

# The loop has ended. Now we figure out WHY it ended.
if guess == CORRECT_PASSWORD:
    print("Access granted.")
else:
    print("Account locked. Try again later.")