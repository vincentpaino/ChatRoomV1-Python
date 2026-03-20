"""
Name: Vincent J. Paino
Date Completed: 2026-03-20
Program Description: This file holds all completed client side functionality for compatibility with
the server side functions defined in server_functions.py. 
"""

# Specs:
# The client first checks the correct usage of the command, and, if correct, sends the command to the server.
# If the server can verify the UserID and the Password, the server will send a confirmation
# message to the client; otherwise, the server will decline login and send an error message to the client.
"""
def is_logged_in(s, BUFFER_SIZE):
    try:
        s.sendall("is_logged_in".encode('utf-8'))
        rec = s.recv(BUFFER_SIZE)
        rec = rec.decode('utf-8')
        if rec == "True":
            return True
        else:
            return False
    except ValueError as e:
        print(f"Error: {e}")
        return False
"""
# Client side checks checks the correct usage of the command 
# including correct lengths of UserID and Password
# Length of UserID = 3-32 chars
# Length of Password = 4-8 chars
def newuser(user_input, is_logged_in, s, BUFFER_SIZE):
    try:
        if not is_logged_in:
            _, UserID, Password = user_input.split()
            if 3 <= len(UserID) <= 32 and 4 <= len(Password) <= 8:
                s.sendall(user_input.encode('utf-8'))
                rec = s.recv(BUFFER_SIZE)
                rec = rec.decode('utf-8')
                print(f"{rec}")
            else:
                print("Denied. Invalid username or password length.")
        else:
            print("Denied. Please logout first.")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return

# The client first checks the correct usage of the command, and, if correct, sends the command to the
# server. If the server can verify the UserID and the Password, the server will send a confirmation
# message to the client; otherwise, the server will decline login and send an error message to the
# client.
def login(user_input, is_logged_in, s, BUFFER_SIZE):
    try:
        if not is_logged_in:
            _, UserID, Password = user_input.split()
            if _ == "login" and UserID and Password: # Check to see if we receive a UserID and Password
                s.sendall(user_input.encode('utf-8'))
                msg = s.recv(BUFFER_SIZE)
                msg = msg.decode('utf-8')
                if msg == "login confirmed":
                    print(msg)
                    is_logged_in = True
                    return is_logged_in
                else:
                    print(msg)
                    return is_logged_in
        else:
            print("Denied. Please logout first.")
            return is_logged_in
    except ValueError as e:
        print(f"Error: {e}")
        return is_logged_in
    
# Send a message to the server. Message size can be between 1 and 256 characters.
def send(user_input, is_logged_in, s, BUFFER_SIZE):
    try:
        if is_logged_in:
            message = user_input[5:]  # Strip the "send " prefix and check the length
            if 1 <= len(message) <= BUFFER_SIZE:
                s.sendall(user_input.encode('utf-8'))
                msg = s.recv(BUFFER_SIZE)
                msg = msg.decode('utf-8')
                print(f"{msg}")
            else:
                return print("Error: Message exceeds buffer size. Please try again with a shorter message.")
        else:
            print("Denied. Please login first.")
        return
    except ValueError as e:
        return
    
# Logout from the chat room. The connection between the server and client will be closed and the
# client should exit. The server should continue running and allow other clients to connect.
def logout(user_input, is_logged_in, s, BUFFER_SIZE):
    try:
        if is_logged_in:
            s.sendall(user_input.encode('utf-8'))
            msg = s.recv(BUFFER_SIZE).decode('utf-8')
            print(msg)
            is_logged_in = False
        else:
            print("Denied. Please login first.")
        return is_logged_in
    except ValueError as e:
        print(f"Error in handle_logout: {e}")
        return is_logged_in