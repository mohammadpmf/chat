import socket, threading, tkinter as tk, tkinter.messagebox as ms
print("Starting Client: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55556))

def f2():
    try:
        while True:
            data = s.recv(1024).decode()
            pretty_point = str(s).find("raddr=") + 6 # 6 ta ham bekhater hamin horoofe raddr=
            addr = str(s)[pretty_point:-1]
            t.set(f"{addr} sent: {data}")
    except:
        ms.showerror("Connection Error.", "Connection Lost!")


def f1(event):
    message = entry.get()
    message = bytes(message, 'utf-8')
    entry.delete(0,tk.END)
    s.sendall(message)

####################################################### tkinter
root = tk.Tk()
root.geometry('600x600+610+200')
entry = tk.Entry(root)
entry.bind("<Return>", f1)
t = tk.StringVar(root)
t.set("Text will be shown here!")
lbl = tk.Label(root, textvariable=t, wraplength=500)
btn = tk.Button(root, text='Send', command=lambda:f1("Alaki String"))
entry.place(relx=0.05, rely=0.05, width=500)
lbl.place(relx=0.05, rely=0.1)
btn.place(relx=0.45, rely=0.85)
###############################################################
threading.Thread(target=f2).start()
tk.mainloop()

