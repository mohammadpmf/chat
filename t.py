from tkinter import Button, filedialog
import tkinter as tk

def o():
    fname = filedialog.askopenfilename()
    print('not good') if fname in ['', ()] else print(fname)
    


root = tk.Tk()

Button(root, text='OK', command=o).pack()

root.mainloop()