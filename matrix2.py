# Binary flags represented as integers
READ = 4       # Binary: 100
WRITE = 2      # Binary: 010
EXECUTE = 1    # Binary: 001

user_permission = 6  # Binary: 110

print("--- Bitwise Testing ---")

if (user_permission & WRITE) == WRITE:
    print("Success: User has WRITE permission.")
else:
    print("Failure: User does not have WRITE permission.")