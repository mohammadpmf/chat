import socket, threading
print("Starting Client: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55555))

def f2():
    data = s.recv(1024).decode()
    pretty_point = str(s).find("raddr=") + 6 # 6 ta ham bekhater hamin horoofe raddr=
    addr = str(s)[pretty_point:-1]
    print(f"{addr} sent: {data}")
    threading.Timer(1, f2).start()

def f1():
    threading.Thread(target=f2).start()
    while True:
        message = input("Enter message: ")
        message = bytes(message, 'utf-8')
        s.sendall(message)


threading.Thread(target=f1).start()
