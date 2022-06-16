from tkinter import Tk, Button, filedialog as fd
def test():
    fname = fd.askopenfilename()
    if fname in ['', ()]:
        print('not good')
    else:
        print(fname)
        # f2name = fd.asksaveasfilename(defaultextension=".espace", filetypes=(("espace file", "*.espace"),("All Files", "*.*")))
        # f2name = fd.asksaveasfile()
        f2name = fd.asksaveasfilename(
            filetypes=(
                ("All Files", "*.*"),
                ("MS Word Files", "*.docx"),
                ("PDF Files", "*.pdf"),
                ("Python Files", '*.py'),
                ("Text Files", '*.txt'),
                ("Video Files", "*.mp4"),
                ("Video Files", "*.mpeg4"),
                ("Video Files", "*.mkv"),
                ("Video Files", "*.avi"),
                ("Audio Files", ("*.mp3", "*.mpeg3", "*.wav")),
                ("Files that start with 'c' :D", "c*.*"),
                ),
            defaultextension=".docx" # ba in pish farz zakhire mikoneh age .pasvand ro nanvisim. Yani vaghti too esm e file . bezarim dg pishfarz ro entekhab nemikoneh.
            )
        print(f2name)
        with open(f2name, 'w') as f:
            f.write('Salam Dadach.')
root = Tk()
Button(root, text='OK', command=test).pack()
root.mainloop()




# # ino ba'd az in ke os ro import kardam kamel taresh kardam ke error nadeh va dar har soorat file e dovvom ro save bokoneh.
# from tkinter import Tk, Button, filedialog as fd
# import os
# def test():
#     fname = fd.askopenfilename()
#     if fname in ['', ()]:
#         print('not good')
#     else:
#         print(fname)
#         # f2name = fd.asksaveasfilename(defaultextension=".espace", filetypes=(("espace file", "*.espace"),("All Files", "*.*")))
#         # f2name = fd.asksaveasfile()
#         f2name = fd.asksaveasfilename(
#             filetypes=(
#                 ("All Files", "*.*"),
#                 ("MS Word Files", "*.docx"),
#                 ("PDF Files", "*.pdf"),
#                 ("Python Files", '*.py'),
#                 ("Text Files", '*.txt'),
#                 ("Video Files", "*.mp4"),
#                 ("Video Files", "*.mpeg4"),
#                 ("Video Files", "*.mkv"),
#                 ("Video Files", "*.avi"),
#                 ("Audio Files", ("*.mp3", "*.mpeg3", "*.wav")),
#                 ("Files that start with 'c' :D", "c*.*"),
#                 ),
#             defaultextension=".docx" # ba in pish farz zakhire mikoneh age .pasvand ro nanvisim. Yani vaghti too esm e file . bezarim dg pishfarz ro entekhab nemikoneh.
#             )
#         print(f2name)
#         if f2name in ['', ()]:
#             dir_path = os.path.dirname(os.path.realpath(__file__))
#             print(dir_path)
#             f2name = f"{dir_path}/default" # barash pasvandi dar nazar nagereftam va jayi ke file ejra shodeh, hamoonja be esme default save esh kardam.
#             print(f2name)
#         with open(f2name, 'w') as f:
#             f.write('Salam Dadach.')
# root = Tk()
# Button(root, text='OK', command=test).pack()
# root.mainloop()