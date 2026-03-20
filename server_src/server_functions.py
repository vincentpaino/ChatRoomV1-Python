"""
Name: Vincent J. Paino
Date Completed: 2026-03-20
Program Description: This file holds all completed server side functionality for compatibility wtih
the client side functions defined in client_functions.py. 
"""

### HELPER FUNCTIONS ##
# Validates login on server side
def validate_login(UserID, Password):
    with open("users.txt", "r") as f:
        for line in f:
            # Remove parentheses and split by the comma
            clean_line = line.strip().replace('(', '').replace(')', '')
            if clean_line:
                parts = clean_line.split(',')
                # Grab the first part, the UserID
                stored_UserID = parts[0].strip()
                # Then, grab the second part, the Password
                stored_Password = parts[1].strip()
                # print(f"[DEBUG] comparing '{UserID}'=='{stored_UserID}' and '{Password}'=='{stored_Password}'")
                if UserID == stored_UserID and Password == stored_Password:
                    return True
    return False

def check_dup_newuser(UserID):
    with open("users.txt", "r") as f:
        for line in f:
            # Remove parentheses and split by the comma
            clean_line = line.strip().replace('(', '').replace(')', '')
            if clean_line:
                # Grab the first part, the UserID
                parts = clean_line.split(',')
                stored_UserID = parts[0].strip()
                # Check if there's a duplicate
                if UserID == stored_UserID:
                    return True
    return False


# Appends a new (UserID, Password) entry to users.txt, creating the file if it doesn't exist
def write_user(UserID, Password):
    with open("users.txt", "a") as f:
        f.write(f"\n({UserID}, {Password})")
    
# Helper for login & send functions to check if the user is logged in or not. Returns a boolean value.
# Don't have to check for spaces in the username/password
# Username: 3-32 characters
# Password: 4-8 characters
def handle_newuser(conn, data, BUFFER_SIZE):
    try:
        _, UserID, Password = data.split()
        UserID = UserID
        Password = Password
        if not check_dup_newuser(UserID):
            write_user(UserID, Password)
            conn.sendall("New user account created. Please login.".encode('utf-8'))
            print("New user account created")
        else:
            conn.sendall("Denied. User account already exists.".encode('utf-8'))
    except Exception as e:
        print(f"Error in handle_newuser: {e}")

# Handles the login command
def handle_login(conn, data, BUFFER_SIZE):
    try:
        _, UserID, Password = data.split()
        UserID = UserID
        Password = Password
        if validate_login(UserID, Password):
            conn.sendall("login confirmed".encode('utf-8'))
            print(UserID + " login.")
            return UserID
        else:
            conn.sendall("Denied. User name or password incorrect.".encode('utf-8'))
            return ""
    except Exception as e:
        print(f"Error in handle_login: {e}")
        return ""
    
# Receives message from client. The server will precede the message with the UserID and send it back. 
def handle_send(conn, data, UserID, BUFFER_SIZE):
    try:
        prefix = UserID
        # Should strip the "send " prefix first
        _, *parts = data.split()
        msg = " ".join(parts)
        msg = f"{prefix}: {msg}"    
        conn.sendall(msg.encode('utf-8'))
        print(msg)
    except Exception as e:
        print(f"Error in handle_send: {e}")

# Handles the logout command by closing the client connection.
# Server still persists whenever client disconnects.
def handle_logout(conn, UserID):
    try:
        msg = UserID + " left."
        conn.sendall(msg.encode('utf-8'))
        print(UserID + " logout")
        conn.close()
    except Exception as e:
        print(f"Error in handle_logout: {e}")