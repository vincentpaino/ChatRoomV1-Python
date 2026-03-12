# The client first checks the correct usage of the command, and, if correct, sends the command to the server.
# If the server can verify the UserID and the Password, the server will send a confirmation
# message to the client; otherwise, the server will decline login and send an error message to the client.

# s = client socket
# BUFFER_SIZE = 256
def login(s, BUFFER_SIZE):
    try:
        print("login ")
        msg = input("")
        s.sendall(msg.encode('utf-8'))
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