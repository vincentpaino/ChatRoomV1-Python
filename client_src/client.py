"""
Name: Vincent J. Paino
Date Completed: 2026-03-20
Program Description: This file holds the logic of a client-side socket in Python. Uses user input to communicate.
"""

import socket
from client_functions import newuser, login, send, logout

# Define global variables
# Logic to keep the program running until the user decides to exit
running = True

# 1 + last 4 digits of student ID
SERVER_PORT = 19489

# Max of 256 characters (fixed) to send a message
BUFFER_SIZE = 256

# Use this server IP address when running client/server on the same device
SERVER_IP = "127.0.0.1" 

# Empty UserID and Password that are to be filled via user input in main logic
UserID = ""
Password = ""

# Global boolean variable to determine if the user logged in successfully or not
is_logged_in = False

# Logic starts here
# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# Connect to a server
try:
    s.connect((SERVER_IP, SERVER_PORT))
    print("My chat room client. Version One.\n")
except socket.error:
    print("Failed to connect to server.")
    s.close()
    running = False

# Main program logic: while the socket is open, 
# the client will wait for user input and send it to the server 
while running:
    user_input = input()
    if user_input.startswith("newuser"):
        newuser(user_input, is_logged_in, s, BUFFER_SIZE)
    elif user_input.startswith("login"):
        is_logged_in = login(user_input, is_logged_in, s, BUFFER_SIZE)
    elif user_input.startswith("send"):
        send(user_input, is_logged_in, s, BUFFER_SIZE)
    elif user_input.startswith("logout"):
        if is_logged_in:
            is_logged_in = logout(user_input, is_logged_in, s, BUFFER_SIZE)
            s.close()
            running = False
        else:
            print("Denied. Please login first.")
    else:
        print("Invalid command.")
        
is_logged_in = False

    