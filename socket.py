import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=78
s.bind((host,port))
s.listen()
print("host name",host)
print("I am server ready to accept your request(Listening)")
while True:
    cs,addr=s.accept()
    print("Connection recieved from",addr[0])
    msg="Thanks for connecting"
    cs.send(masg.encode("UTF-8"))
    while True:
        msg2=cs.recv(1024)
        if msg2:
            print(msg2.decode("UTF-8"))
        msg1=input("Type a message for client")
        if msg1:
            cs.send(msg.encode("UTF-8"))
            
