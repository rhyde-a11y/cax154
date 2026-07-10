Correct_password="python123"
max_attempts=4
attempts=0

guess=""
while guess != Correct_password and attempts < max_attempts:
    guess=input("Enter password: ")
    if guess != Correct_password:
        attempts += 1
        remaining=max_attempts-attempts
        print(f"Try again! Attempts remaining: {remaining}")

if guess == Correct_password:
    print("Access permitted.")
else:
    print("Account locked. Contact support.")