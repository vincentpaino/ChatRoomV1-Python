import socket

#
working = True

# 1 + last 4 digits of student ID
SERVER_PORT = 19489

# Use this when running client/server on the same device
SERVER_IP = "127.0.0.1" 

BUFFER_SIZE = 256

# Empty UserID and Password that are to be filled via user input
UserID = ""
Password = ""

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the web server on port 80 - the normal http port
if s.connect(("www.python.org", SERVER_PORT)):
    print("My chat room client. Version One.")
    print("\n")
    



while working:
    input = input()
    

### FUNCTIONS WRITTEN HERE ###
# For login, user is expected to write a valid username and password in the form "username password" that matches with one tuple in users.txt. 
# Whether this is successful or not, the server will respond with a message that is printed on the client side.

    