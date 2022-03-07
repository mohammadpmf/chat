import socket, threading, tkinter as tk, tkinter.messagebox as ms
print ("Starting server: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55556))
s.listen()
conn, addr = s.accept()

def f2(event):
    # message = input("Enter message: ")
    message = entry.get()
    message = bytes(message, 'utf-8')
    entry.delete(0,tk.END)
    conn.sendall(message)

def f1():
    try:
        # threading.Thread(target=f2).start()
        ms.showinfo('Successfull Connection', f'Connected by {addr}')
        while True:
            data = conn.recv(1024).decode()
            t.set(f"{addr} sent: {data}")
    except:
        ms.showerror("Connection Error.", "Connection Lost!")

####################################################### tkinter
root = tk.Tk()
root.geometry('600x600+10+200')
entry = tk.Entry(root)
entry.bind("<Return>", f2)
t = tk.StringVar(root)
t.set("Text will be shown here!")
lbl = tk.Label(root, textvariable=t, wraplength=500)
btn = tk.Button(root, text='Send', command=lambda:f2("Alaki String"))
entry.place(relx=0.05, rely=0.05, width=500)
lbl.place(relx=0.05, rely=0.1)
btn.place(relx=0.45, rely=0.85)
###############################################################
threading.Thread(target=f1).start()
tk.mainloop()

