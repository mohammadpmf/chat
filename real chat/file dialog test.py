from tkinter import Tk, Button, filedialog
def test():
    fname = filedialog.askopenfilename()
    if fname in ['', ()]:
        print('not good')
    else:
        print(fname)
        fhandle = open(fname, 'rb')
        print(fhandle.read())
root = Tk()
Button(root, text='OK', command=test).pack()
root.mainloop()