import math
import platform
import random


def main():
    # 1. Generate a random integer between 1 and 100
    random_num = random.randint(1, 100)

    # 2. Calculate square root and round down (floor)
    sqrt_floored = math.floor(math.sqrt(random_num))

    # 3. Get OS name and Python version
    os_name = platform.system()
    python_ver = platform.python_version()

    # Output the results
    print(f"Random Number: {random_num}")
    print(f"Square Root (floored): {sqrt_floored}")
    print(f"Operating System: {os_name}")
    print(f"Python Version: {python_ver}")
  

if __name__ == "__main__":
    main()