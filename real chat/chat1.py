import socket
import threading
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import filedialog as fd
from tkinter import scrolledtext
from datetime import datetime

# print ("Starting server: ")
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 55556))
# s.listen()
# conn, addr = s.accept()
# print(conn)
# print(addr)

# def f2(event):
#     # message = input("Enter message: ")
#     message = entry.get()
#     message = bytes(message, 'utf-8')
#     entry.delete(0,tk.END)
#     conn.sendall(message)
#     now = datetime.now()
#     date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#     previous = t.get() + '\n'
#     t.set(f"{previous}{message.decode()}\t\t\t\t\tsent at {date_time}")

# def f1():
#     try:
#         # threading.Thread(target=f2).start()
#         msb.showinfo('Successfull Connection', f'Connected by {addr}')
#         lbl_frame.config(text=f"You are chatting with {addr}")
#         while True:
#             now = datetime.now()
#             date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#             data = conn.recv(1024).decode()
#             previous = t.get() + '\n'
#             t.set(f"{previous}Recived: {data}\t\t\t\t\tat {date_time}")
#     except:
#         msb.showerror("Connection Error.", "Connection Lost!")

# def clear(event='Alaki event'):
#     t.set("")
    
# def send_file():
#     def send_it(fname):
#         with open(fname, 'rb') as f:
#             data = f.read()
#             conn.sendall(data)
#         msb.showinfo("Sent!", f"{fname}'s Data Sent!\n But I'm not sure the receiver got it completely :D")
#     file_name = fd.askopenfilename()
#     if file_name in ['', ()]: # User didn't choose any file
#         return
#     threading.Thread(target=send_it, args=(file_name,)).start()


####################################### UI #######################################
root = tk.Tk()
root.title("Chat")
root.config(bg='dark cyan')
# root.bind("<Delete>", clear)
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
root.geometry(f"{SCREEN_WIDTH//2}x{SCREEN_HEIGHT//2}")
frame_sent_messages = tk.LabelFrame(root, bg='sky blue', text='Your ip')
frame_received_messages = tk.LabelFrame(root, bg='light green', text='You are chatting with: others ip')
frame_messages = tk.LabelFrame(root, bg='light cyan')
frame_sent_messages.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.80)
frame_received_messages.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.80)
frame_messages.place(relx=0.01, rely=0.82, relwidth=0.98, relheight=0.17)
text_area = scrolledtext.ScrolledText(frame_messages, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman",15))
text_area.pack(side='top', fill='both', padx=2, pady=2)
text_area.focus()
# text_area.bind("<Return>", f2)

# lbl_frame = ttk.Labelframe(root, text="Chat Box")
# t = tk.StringVar(root)
# lbl = tk.Label(lbl_frame, textvariable=t, wraplength=SCREEN_WIDTH*0.9)
# frame_btns = tk.Frame(root, bg='sky blue')
# btn_send_file = tk.Button(frame_btns, text='Send File ...', command=send_file)
# btn = tk.Button(frame_btns, text='Send', command=lambda:f2("Alaki String"))
# btn_clear = tk.Button(frame_btns, text='Clear', command=clear)
# btn_exit = tk.Button(frame_btns, text='End Chat', command=root.destroy)

# lbl_frame.pack(side='top', expand=True, fill='both', padx=8, pady=4)
# lbl.pack(expand=True, fill='both', padx=8, pady=4)
# frame_btns.pack(side='bottom', padx=8, pady=4, fill='x')
# btn_send_file.pack(side='left', padx=40, expand=1)
# btn_exit.pack(side='right', padx=40, pady=3)
# btn_clear.pack(side='right', padx=40, pady=3)
# btn.pack(side='right', padx=40, pady=3)
# ####################################### End UI #######################################
# threading.Thread(target=f1).start()
root.mainloop()
