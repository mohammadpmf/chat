import socket, threading, tkinter as tk, tkinter.ttk as ttk, tkinter.messagebox as msb
from datetime import datetime
from tkinter import filedialog as fd
MY_WIDTH = 900

print("Starting Client: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55556))
pretty_point = str(s).find("raddr=") + 6 # 6 ta ham bekhater hamin horoofe raddr=
addr = str(s)[pretty_point:-1]


def f2():
    try:
        lbl_frame.config(text=f"You are chatting with {addr}")
        while True:
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            data = s.recv(1024).decode()
            previous = t.get() + '\n'
            t.set(f"{previous}Recived: {data}\t\t\t\t\tat {date_time}")
    except:
        msb.showerror("Connection Error.", "Connection Lost!")


def f1(event):
    message = entry.get()
    message = bytes(message, 'utf-8')
    entry.delete(0,tk.END)
    s.sendall(message)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    previous = t.get() + '\n'
    t.set(f"{previous}{message.decode()}\t\t\t\t\tsent at {date_time}")

def clear(event='Alaki event'):
    t.set("")


def send_file():
    def send_it(fname):
        with open(fname, 'rb') as f:
            data = f.read()
            s.sendall(data)
        msb.showinfo("Sent!", f"{fname}'s Data Sent!\n But I'm not sure the receiver got it completely :D")
    file_name = fd.askopenfilename()
    if file_name in ['', ()]: # User didn't choose any file
        return
    threading.Thread(target=send_it, args=(file_name,)).start()


####################################################### tkinter
root = tk.Tk()
root.config(bg='sky blue')
root.title("Chat2")
root.geometry(f'{MY_WIDTH}x600+0+200')
root.bind("<Delete>", clear)
lbl_frame = ttk.Labelframe(root, text="Chat Box")
entry = tk.Entry(root)
entry.bind("<Return>", f1)
t = tk.StringVar(lbl_frame)
lbl = tk.Label(lbl_frame, textvariable=t, wraplength=MY_WIDTH*0.9)
frame_btns = tk.Frame(root, bg='sky blue')
btn_send_file = tk.Button(frame_btns, text='Send File ...', command=send_file)
btn = tk.Button(frame_btns, text='Send', command=lambda:f1("Alaki String"))
btn_clear = tk.Button(frame_btns, text='Clear', command=clear)
btn_exit = tk.Button(frame_btns, text='End Chat', command=root.destroy)

entry.pack(side='top', fill='x', padx=8, pady=4)
lbl_frame.pack(side='top', expand=True, fill='both', padx=8, pady=4)
lbl.pack(expand=True, fill='both', padx=8, pady=4)
frame_btns.pack(side='bottom', padx=8, pady=4, fill='x')
btn_send_file.pack(side='left', padx=40, expand=1)
btn_exit.pack(side='right', padx=40, pady=3)
btn_clear.pack(side='right', padx=40, pady=3)
btn.pack(side='right', padx=40, pady=3)
###############################################################
threading.Thread(target=f2).start()
tk.mainloop()

