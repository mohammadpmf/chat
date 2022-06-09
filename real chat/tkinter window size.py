from tkinter import *
win= Tk()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
win.geometry(f"{screen_width//2}x{screen_height//2}")
print("Screen width:", screen_width)
print("Screen height:", screen_height)
win.mainloop()