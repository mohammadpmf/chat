import socket
import threading
import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import filedialog as fd
from tkinter import scrolledtext
from datetime import datetime


def choose_file(destination="Unknown person!!!"):
    file_name = fd.askopenfilename()
    if file_name in ['', ()]:
        msb.showwarning("No file selected!", "You should choose a File!")
    else:
        if msb.askyesno("Confirmation?", f"Are you sure you want to send file {file_name} to {destination}?"):
            new_thread = threading.Thread(target=send_file, args=(file_name,))
            new_thread.setDaemon(True)
            new_thread.start()
        else:
            msb.showinfo("OK", f"File did not send to {destination}.")
