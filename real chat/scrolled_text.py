import tkinter as tk
from tkinter import scrolledtext
win = tk.Tk()
text_area = scrolledtext.ScrolledText(
    win, wrap = tk.WORD, width = 40, height = 10,
    font = ("Times New Roman",15))
text_area.grid(column = 0, pady = 10, padx = 10)
text_area.focus()
win.mainloop()
