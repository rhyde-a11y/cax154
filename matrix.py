# Binary flags represented as integers
READ = 4       # Binary: 100
WRITE = 2      # Binary: 010
EXECUTE = 1    # Binary: 001

# A user with READ and WRITE permissions (4 + 2)
user_permission = 6  # Binary: 110

print("--- Bitwise Testing ---")
# Bitwise AND compares the bits:
#   110  (user_permission)
# & 010  (WRITE)
# -------
#   010  (Which equals 2, which matches WRITE!)
if (user_permission & WRITE) == WRITE:
    print("Success: User has WRITE permission.")
else:
    print("Failure: User does not have WRITE permission.")