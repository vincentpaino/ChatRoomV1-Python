"""
Name: Vincent J. Paino
Date Completed: 2026-03-20
Program Description: This file holds all the logic necessary to run a server-side socket in Python.
"""

import socket
from server_functions import handle_newuser, handle_login, handle_send, handle_logout

# Define global variables
# Logic to keep the server running
running = True

# 1 + last 4 digits of student ID
SERVER_PORT = 19489

# Use localhost when running client/server on the same device
SERVER_IP = "127.0.0.1" 

# Max of 256 characters (fixed) to send a message
BUFFER_SIZE = 256

# Initialize an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This line allows us to re-use the server port immediately after the server stops
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to local host (connects to itself) and our unique server port in tuple format
server_socket.bind((SERVER_IP, SERVER_PORT))

# Begin listening for incoming connections (only need to call this once)
server_socket.listen(5)

print("My chat room server. Version One.\n")

# Outer loop: keeps the server running indefinitely, accepting new clients after each logout
while running:
    # Block until a client connects
    conn, addr = server_socket.accept()

    # Track the currently logged-in UserID for this session
    UserID = ""

    # Inner loop: keep receiving commands from the connected client until they logout
    while running:
        try:
            data = conn.recv(BUFFER_SIZE).decode('utf-8')

            if data.startswith("newuser"):
                handle_newuser(conn, data, BUFFER_SIZE)
            elif data.startswith("login"):
                UserID = handle_login(conn, data, BUFFER_SIZE)
            elif data.startswith("send"):
                handle_send(conn, data, UserID, BUFFER_SIZE)
            elif data.startswith("logout"):
                handle_logout(conn, UserID)
                break  # Exit inner loop, go back to waiting for a new client

        except Exception as e:
            print(f"Error: {e}")
            conn.close()
            break





    



