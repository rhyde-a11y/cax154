import hashlib
from difflib import SequenceMatcher

def hash_file(file_path1, file_path2):
    # Use hashlib to store the hash of a file
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    # Read and hash the first file
    with open(file_path1, "rb") as file:
        while True:
            chunk = file.read(1024)
            if not chunk:  # Stop when the end of the file is reached (empty bytes)
                break
            h1.update(chunk)
            
    # Read and hash the second file
    with open(file_path2, "rb") as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            h2.update(chunk)

    # return the hex digests
    return h1.hexdigest(), h2.hexdigest()

# --- GET FILE PATHS FROM USER ---
# .strip("'\"") automatically removes any accidental quotes 
# (which often happens if a user drags and drops a file into the terminal)
file1 = input("Enter the path for the first file: ").strip("'\"")
file2 = input("Enter the path for the second file: ").strip("'\"")

# Run the function
try:
    msg1, msg2 = hash_file(file1, file2)

    if msg1 != msg2:
        print("\n❌ These files are not identical.")
    else:
        print("\n✅ These files are identical.")
        
except FileNotFoundError as e:
    print(f"\nError: Could not find the file. Please check the path and try again.\nDetails: {e}")