import socket

# 1 + last 4 digits of student ID
SERVER_PORT = 19489

# Use this when running client/server on the same device
SERVER_IP = "127.0.0.1" 

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), SERVER_PORT))

# become a server socket
serversocket.listen(5)

# When we read the data from users.txt on the server start, we store it in two arrays respectively
UserIDs=[]
Passwords=[]

if serversocket:
    print("My chat room server. Version One.")
    print("\n")
    
else:
    print("Error: Could not create server socket please retry again.")

### FUNCTIONS WRITTEN HERE ###


    



