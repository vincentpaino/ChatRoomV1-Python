"""
Script to test code to be implemented in the "_functions.py" files.
"""

input = input("Enter proper login command: ")
_, UserID, Password = input.split()
# maxsplit=1 ensures only the first space is used as a delimiter, 
# so the second variable gets the rest of the string.

print(f"command: {_}")
print(f"UserID: {UserID}")
print(f"Password: {Password}")

print("\n")
print("UserID test:\n")

UserID = "Vincent"
prefix = UserID + ": "
print(f"{prefix}")
