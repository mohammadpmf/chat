import socket, threading
print ("Starting server: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555))
s.listen()
conn, addr = s.accept()

def f2():
    message = input("Enter message: ")
    message = bytes(message, 'utf-8')
    conn.sendall(message)
    f2()

def f1():
    try:
        threading.Thread(target=f2).start()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            print(f"{addr} sent: {data}")
    except:
        print("Connection Lost!")


threading.Thread(target=f1).start()