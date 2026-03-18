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

# Client side checks checks the correct usage of the command 
# including correct lengths of UserID and Password
# Length of UserID = 3-32 chars
# Length of Password = 4-8 chars
def newuser(input, s, BUFFER_SIZE):
    try:
        return
    except:
        return

# s = client socket
# BUFFER_SIZE = 256
def login(input, s, BUFFER_SIZE):
    try:
        if (is_logged_in):
            s.sendall(input.encode('utf-8'))
            rec = s.recv(BUFFER_SIZE)
            rec = rec.decode('utf-8')
            print(f"{rec}")
            if rec == "login confirmed":
                return True
            else:
                return False
    except ValueError as e:
        print(f"Error: {e}")
        return False
    
# Description: Send the “message” to the server. Message size can be between 1 and 256 characters.
def send(input, s, BUFFER_SIZE):
    try:
        if input.size() < BUFFER_SIZE:
            s.sendall(input.encode('utf-8'))
        else:
            return print("Error: Message exceeds buffer size. Please try again with a shorter message.")
        return
    except:
        return

def logout(input, s, BUFFER_SIZE):
    try:
        if is_logged_in and input == "logout":
            msg = s.recv()
            print(f"{msg}")
            s.close()
        else:
            print("Incorrect usage of logout command. Please try again.")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return