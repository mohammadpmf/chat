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

def f2(event):
    pass
#     # message = input("Enter message: ")
#     message = entry.get()
#     message = bytes(message, 'utf-8')
#     entry.delete(0,tk.END)
#     conn.sendall(message)
#     now = datetime.now()
#     date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#     previous = t.get() + '\n'
#     t.set(f"{previous}{message.decode()}\t\t\t\t\tsent at {date_time}")

def f1():
    pass
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

def clear(event='Alaki event'):
    pass
#     t.set("")
    
def send_file():
    pass
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
frame_btns = tk.LabelFrame(root, bg='dark cyan')
frame_sent_messages.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.8)
frame_received_messages.place(relx=0, rely=0, relwidth=0.5, relheight=0.8)
frame_messages.place(relx=0.2, rely=0.805, relwidth=0.8, relheight=0.2)
frame_btns.place(relx=0, rely=0.805, relwidth=0.2, relheight=0.2)
text_area = scrolledtext.ScrolledText(frame_messages, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman",15))
text_area.pack(side='top', fill='both', padx=2, pady=2)
text_area.focus()
# text_area.bind("<Return>", f2)
t = tk.StringVar(frame_sent_messages)
lbl_sent_messages = tk.Label(frame_sent_messages, text='test')
lbl_time_sent_messages = tk.Label(frame_sent_messages, text='time')
lbl_received_messages = tk.Label(frame_received_messages, text='test 2')
lbl_time_received_messages = tk.Label(frame_received_messages, text='time 2')

lbl_sent_messages.place(relx=0.01, rely=0.01, relwidth=0.7, relheight=0.98)
lbl_time_sent_messages.place(relx=0.72, rely=0.01, relwidth=0.27, relheight=0.98)
lbl_received_messages.place(relx=0.01, rely=0.01, relwidth=0.7, relheight=0.98)
lbl_time_received_messages.place(relx=0.72, rely=0.01, relwidth=0.27, relheight=0.98)

btn_send_file = tk.Button(frame_btns, text='Send File ...', command=send_file, font=('', 6))
btn_send_message = tk.Button(frame_btns, text='Send', command=lambda:f2("Alaki String"), font=('', 10))
btn_clear = tk.Button(frame_btns, text='Clear', command=clear, font=('', 10))
btn_exit = tk.Button(frame_btns, text='Exit', command=root.destroy, font=('', 10))

btn_send_file.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.4)
btn_send_message.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.4)
btn_clear.place(relx=0.55, rely=0.55, relwidth=0.4, relheight=0.4)
btn_exit.place(relx=0.05, rely=0.55, relwidth=0.4, relheight=0.4)
# ####################################### End UI #######################################
# threading.Thread(target=f1).start()
root.mainloop()
