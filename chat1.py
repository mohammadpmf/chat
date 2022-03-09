from email import message
import socket, threading, tkinter as tk, tkinter.ttk as ttk, tkinter.messagebox as msb
from datetime import datetime
MY_WIDTH = 900

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
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    previous = t.get() + '\n'
    t.set(f"{previous}{message.decode()}\t\t\t\t\tsent at {date_time}")

def f1():
    try:
        # threading.Thread(target=f2).start()
        msb.showinfo('Successfull Connection', f'Connected by {addr}')
        lbl_frame.config(text=f"You are chatting with {addr}")
        while True:
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            data = conn.recv(1024).decode()
            previous = t.get() + '\n'
            t.set(f"{previous}Recived: {data}\t\t\t\t\tat {date_time}")
    except:
        msb.showerror("Connection Error.", "Connection Lost!")

def clear(event='Alaki event'):
    t.set("")
    

####################################################### tkinter
root = tk.Tk()
root.config(bg='sky blue')
root.title("Chat1")
root.geometry(f'{MY_WIDTH}x600+0+200')
root.bind("<Delete>", clear)
lbl_frame = ttk.Labelframe(root, text="Chat Box")
entry = tk.Entry(root)
entry.bind("<Return>", f2)
t = tk.StringVar(root)
lbl = tk.Label(lbl_frame, textvariable=t, wraplength=MY_WIDTH*0.9)
frame_btns = tk.Frame(root, bg='sky blue')
btn = tk.Button(frame_btns, text='Send', command=lambda:f2("Alaki String"))
btn_clear = tk.Button(frame_btns, text='Clear', command=clear)
btn_exit = tk.Button(frame_btns, text='End Chat', command=root.destroy)

entry.pack(side='top', fill='x', padx=8, pady=4)
lbl_frame.pack(side='top', expand=True, fill='both', padx=8, pady=4)
lbl.pack(expand=True, fill='both', padx=8, pady=4)
frame_btns.pack(side='bottom', padx=8, pady=4)
btn.pack(side='left', padx=40, pady=3, expand=1)
btn_clear.pack(side='left', padx=40, pady=3)
btn_exit.pack(side='right', padx=40, pady=3)
###############################################################
threading.Thread(target=f1).start()
tk.mainloop()
