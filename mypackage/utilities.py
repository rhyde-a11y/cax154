import math


def greet(name: str) -> str:
    """Returns a greeting string for the given name."""
    return f"Hello, {name}!"


def factorial(n: int) -> int:
    """Returns the factorial of n using the math module."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    return math.factorial(n)


def main():
    # Prompt the user for their name
    user_name = input("Enter your name: ")

    # Strip extra whitespace in case they hit spacebar by accident
    user_name = user_name.strip()

    # Fallback to a default name if they just press Enter
    if not user_name:
        user_name = "Friend"

    # Call the greet function with the user's input
    greeting_message = greet(user_name)
    print(greeting_message)


if __name__ == "__main__":
    main()