import socket
cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=78
cs.connect((host,port))
msg=cs.recv(1024)
print(msg.decode("UTF-8"))
while True:
    msg1=input("enter message for server=")
    if msg1:
        cs.send(msg1.encode("UTF-8"))
    msg2=cs.recv(1024)
    print(msg2.decode("UTF-8"))
