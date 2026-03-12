# Write corresponding server side functionality

# Reads the UserIDs from users.txt and stores them in the UserIDs array at runtime.
def read_userID(UserIDs):
    try:
        # 'with' keyword closes file automatically
        with open("users.txt", "r") as f:
            for line in f:
                # Remove parentheses and split by the comma
                clean_line = line.strip().replace('(', '').replace(')', '')
                if clean_line:
                    # Grab the first part (the UserID)
                    parts = clean_line.split(',')
                    UserID = parts[0].strip()
                    UserIDs.append(UserID)
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Reads the Passwords from users.txt and stores them in the Passwords array at runtime.
def read_password(Passwords):
    try:
        # 'with' keyword closes file automatically
        with open("users.txt", "r") as f:
            for line in f:
                # Remove parentheses and split by the comma
                clean_line = line.strip().replace('(', '').replace(')', '')
                if clean_line:
                    # Grab the first part (the UserID)
                    parts = clean_line.split(',')
                    Password = parts[1].strip()
                    Passwords.append(Password)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    
def store_input_userID_and_password():
    return

# s = server socket
# BUFFER_SIZE = 256
def login(s, BUFFER_SIZE):
    try:

    except ValueError as e:
        print(f"Error: {e}")
        return False