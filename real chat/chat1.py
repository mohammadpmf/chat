import socket
import threading
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import filedialog as fd
from tkinter import scrolledtext
from datetime import datetime

IP = '127.0.0.1'
PORT = 55558
print ("Starting server: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen()
conn, addr = s.accept()
print(conn)
print(addr)
laddr_point = str(conn).find("laddr=")
laddr_point += 6 # 6 ta ham bekhater hamin horoofe laddr=
raddr_point = str(conn).find("raddr=")
raddr_point += 6 # 6 ta ham bekhater hamin horoofe raddr=
laddr = str(conn)[laddr_point:raddr_point-6-2] # -6 bekhatere ine ke raddr= ro ezafe karde boodam. -2 be khatere ine ke , va space e akhar nayofteh.
raddr = str(conn)[raddr_point:-1] # ta -1 be khatere ine ke alamate > nayofteh.
print(f"{laddr=}\n{raddr=}")


def choose_file():
    file_name = fd.askopenfilename()
    if file_name in ['', ()]:
        msb.showwarning("No file selected!", "You should choose a File!")
    else:
        if msb.askyesno("Confirmation?", f"Are you sure you want to send file {file_name} to {raddr}?"):
            new_thread = threading.Thread(target=send_file, args=(file_name,))
            new_thread.setDaemon(True)
            new_thread.start()
        else:
            msb.showinfo("OK", "File did not send.")

def refresh_messages():
    sent_message.set('\n'.join(list_sent_messages))
    sent_message_time.set('\n'.join(list_sent_messages_time))
    received_message.set('\n'.join(list_received_messages))
    received_message_time.set('\n'.join(list_received_messages_time))


def send_message_function(event):
    message = text_area.get("1.0", 'end-1c')
    text_area.delete("1.0", 'end')
    message = message.strip()
    if message != "":
        try:
            conn.sendall(("M" + message).encode()) # avvalesh ye M bozorg ezafe kardam ke yani message hast in peygham.
            list_sent_messages.append(message)
            list_sent_messages_time.append(datetime.now().strftime("%H:%M:%S"))
            refresh_messages()
        except BrokenPipeError:
            msb.showerror("Connection Error.", "The Pipe is Broken :(")


def receive_message_function():
    try:
        msb.showinfo('Successfull Connection', f'Connected by {raddr}')
        frame_received_messages.config(text=f"You are chatting with: {raddr}")
        frame_sent_messages.config(text=f"You Info: {laddr}")
        while True:
            data = conn.recv(1024).decode()
            list_received_messages.append(data)
            list_received_messages_time.append(datetime.now().strftime("%H:%M:%S"))
            refresh_messages()
    except:
        msb.showerror("Connection Error.", "Connection Lost!")
        

def clear(event='Alaki event'):
    list_received_messages.clear()
    list_received_messages_time.clear()
    list_sent_messages.clear()
    list_sent_messages_time.clear()
    sent_message.set('')
    sent_message_time.set('')
    received_message.set('')
    received_message_time.set('')
    text_area.delete("1.0", 'end')
    
def send_file(file_name):
    with open(file_name, 'rb') as f:
        data = f.read().decode()
        data = "F" + data # avvalesh ye F bozorg ezafe kardam ke yani file hast in data.
        data = data.encode()
        conn.sendall(data)
    msb.showinfo("Sent!", f"{file_name}'s Data Sent!\n But I'm not sure the receiver got it completely :D")



list_received_messages = []
list_sent_messages = []
list_received_messages_time = []
list_sent_messages_time = []
####################################### UI #######################################
root = tk.Tk()
root.title("Chat Server")
root.config(bg='dark cyan')
root.bind("<Delete>", clear)
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
root.geometry(f"{SCREEN_WIDTH//2}x{SCREEN_HEIGHT//2}+{SCREEN_WIDTH//2}+{SCREEN_HEIGHT//4}")
frame_sent_messages = tk.LabelFrame(root, bg='sky blue', text='Your Info')
frame_received_messages = tk.LabelFrame(root, bg='light green', text='You are chatting with ...')
frame_messages = tk.LabelFrame(root, bg='light cyan')
frame_btns = tk.LabelFrame(root, bg='dark cyan')
frame_sent_messages.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.8)
frame_received_messages.place(relx=0, rely=0, relwidth=0.5, relheight=0.8)
frame_messages.place(relx=0.2, rely=0.805, relwidth=0.8, relheight=0.2)
frame_btns.place(relx=0, rely=0.805, relwidth=0.2, relheight=0.2)
text_area = scrolledtext.ScrolledText(frame_messages, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman",15))
text_area.pack(side='top', fill='both', padx=2, pady=2)
text_area.focus()
text_area.bind("<End>", send_message_function)
sent_message = tk.StringVar(frame_sent_messages)
sent_message_time = tk.StringVar(frame_sent_messages)
received_message = tk.StringVar(frame_sent_messages)
received_message_time = tk.StringVar(frame_sent_messages)
lbl_sent_messages = tk.Label(frame_sent_messages, textvariable=sent_message, anchor='nw')
lbl_time_sent_messages = tk.Label(frame_sent_messages, textvariable=sent_message_time, anchor='n')
lbl_received_messages = tk.Label(frame_received_messages, textvariable=received_message, anchor='nw')
lbl_time_received_messages = tk.Label(frame_received_messages, textvariable=received_message_time, anchor='n')

lbl_sent_messages.place(relx=0.01, rely=0.01, relwidth=0.75, relheight=0.98)
lbl_time_sent_messages.place(relx=0.77, rely=0.01, relwidth=0.22, relheight=0.98)
lbl_received_messages.place(relx=0.01, rely=0.01, relwidth=0.75, relheight=0.98)
lbl_time_received_messages.place(relx=0.77, rely=0.01, relwidth=0.22, relheight=0.98)

btn_send_file = tk.Button(frame_btns, text='Send File ...', command=choose_file, font=('', 6))
btn_send_message = tk.Button(frame_btns, text='Send', command=lambda:send_message_function("Alaki String"), font=('', 10))
btn_clear = tk.Button(frame_btns, text='Clear', command=clear, font=('', 10))
btn_exit = tk.Button(frame_btns, text='Exit', command=root.destroy, font=('', 10))

btn_send_file.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.4)
btn_send_message.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.4)
btn_clear.place(relx=0.55, rely=0.55, relwidth=0.4, relheight=0.4)
btn_exit.place(relx=0.05, rely=0.55, relwidth=0.4, relheight=0.4)
# ####################################### End UI #######################################

# ####################################### Threads #######################################
thread_send_text = threading.Thread(target=receive_message_function)
thread_send_text.setDaemon(True)
thread_send_text.start()
thread_receive_text = threading.Thread(target=send_message_function, args=("Alaki string", ))
thread_receive_text.setDaemon(True)
thread_receive_text.start()
# ####################################### End Threads #######################################

root.mainloop()
