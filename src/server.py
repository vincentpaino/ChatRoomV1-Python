import socket
from server_functions import handle_newuser, handle_login, handle_send, handle_logout

# 1 + last 4 digits of student ID
SERVER_PORT = 19489

# Max of 256 characters (fixed) to send a message
BUFFER_SIZE = 256

# Use this when running client/server on the same device
SERVER_IP = "127.0.0.1" 

# Initialize an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a well-known port
server_socket.bind((socket.gethostname(), SERVER_PORT))

# When we read the data from users.txt on the server start, we store it in two arrays respectively
# UserIDs=[]
# Passwords=[]

UserID = ""
Password = ""

if server_socket:
    # Listen indefinitely until program termination
    server_socket.listen(5)
    
    # Accept an incoming connection. This call blocks execution until a client connects
    # conn = the connection object
    # addr = A tuple containing the connection details of the remote client (trivial for this program)
    conn, addr = server_socket.accept()
    
    print("My chat room server. Version One.")
    print("\n")
    
    data = conn.recv(1024)
    if data.startswith("newuser "):
        handle_newuser(conn)
        
    elif data.startswith("login "):
        handle_login(conn)
    
    elif data.startswith("send "):
        handle_send(conn, BUFFER_SIZE, UserID)
    
    elif data.startswith("logout "):
        handle_logout(conn, UserID)
        
else:
    print("Error: Could not create server socket please retry again.")





    



