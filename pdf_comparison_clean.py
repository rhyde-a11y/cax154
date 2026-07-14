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

# --- DEFINE YOUR FILE PATHS HERE ---
# Windows Example: "C:/Users/Username/Documents/file1.pdf"
# Mac/Linux Example: "/Users/Username/Documents/file1.pdf"
# Relative Example (if in the same folder): "file1.pdf"

file1 = "path/to/your/first_file.pdf" 
file2 = "path/to/your/second_file.pdf"

# Run the function
msg1, msg2 = hash_file(file1, file2)

if msg1 != msg2:
    print("These files are not identical.")
else:
    print("These files are identical.")