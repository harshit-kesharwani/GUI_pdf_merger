import tkinter
from tkinter import *
from tkinter import  filedialog
from PIL import ImageTk, Image
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox

def file_opener():
   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
       print(i)
def main_window():

    wind = tkinter.Tk()
    wind.configure(background='#0B023D')
    wind.title("Pdf merge")
    windoww = LabelFrame( background='#0B023D',bd=0)
    windoww.grid(row=0, column=0)
    f1 = Label(windoww, text="PDF Merger", font=('Helvetica', 20, 'bold'), fg="#1F77F9", bg='#0B023D')
    f1.grid(row=0, pady=20, sticky=E + W)
    window = LabelFrame(windoww, background='#0B023D')
    window.grid(row=1, column=0, padx=30, pady=10)

    frame = LabelFrame(window, padx=20, pady=20, bg="#1E0A4E", fg="pink",bd=0)
    frame.grid(row=0, column=0, padx=5, pady=5)
    sk = Label(frame, text="FIRST PDF", font=('Helvetica', 11, 'bold'), bg="#1E0A4E", fg="white", borderwidth=1, relief='groove')
    sk.grid(row=0, sticky=W+E)
    sk = Label(frame, text="Insert The Second PDF ", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(frame, text="Click OPEN to continue", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=2, sticky=W)
    b = Button(frame, text="INSERT",  width=20, fg='white', bg='#1F77F9',font=('Helvetica',10,'bold'), bd=0)
    b.grid(row=3,  pady=5)



    far2 = LabelFrame(window, padx=20, pady=20, bg="#1E0A4E", fg="pink", bd=0)
    far2.grid(row=0, column=1, padx=5, pady=5)
    sk = Label(far2, text="SECOND PDF", font=('Helvetica', 11, 'bold'), bg="#1E0A4E", fg="white", borderwidth=1, relief='groove')
    sk.grid(row=0, sticky=W + E)
    sk = Label(far2, text="Insert The Second PDF", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(far2, text="Click INSERT to continue", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=2, sticky=W)
    e = Button(far2, text="INSERT",command=lambda:file_opener(),  width=20, fg='white', bg='#1F77F9', font=('Helvetica',10,'bold'), bd=0)
    e.grid(row=3, pady=5)




main_window()
mainloop()