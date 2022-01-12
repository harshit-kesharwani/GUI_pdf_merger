import tkinter
from tkinter import *
from tkinter import  filedialog
from PIL import ImageTk, Image
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PyPDF2 import PdfFileMerger
merger = PdfFileMerger(strict=False)
x=[]
def file_opener():
   input = filedialog.askopenfilename()

   x.append(input)



def file_merger():
    for files in x:
        merger.append(files)
    merger.write('./Lecture Complete.pdf')
    messagebox.showinfo('PDF merger', 'Merged successfully')
    merger.close()

def main_window():

    wind = tkinter.Tk()
    wind.configure(background='gray99')
    wind.title("Pdf merge")
    windoww = LabelFrame( background='gray',bd=0)
    windoww.grid(row=0, column=0)
    f1 = Label(windoww, text="PDF Merger", font=('Helvetica', 20, 'bold'), fg="snow", bg='gray')
    f1.grid(row=0, pady=15)
    window = LabelFrame(windoww, background='gray99')
    window.grid(row=1, column=0, padx=15, pady=10)

    frame = LabelFrame(window, padx=20, pady=20, bg="gray", fg="pink",bd=0)
    frame.grid(row=0, column=0, padx=5, pady=5)
    sk = Label(frame, text="FIRST PDF", font=('Helvetica', 15, 'bold'), bg="gray", fg="white", borderwidth=1, relief='raised')
    sk.grid(row=0, sticky=W+E)
    sk = Label(frame, text="Insert The FIRST PDF ", font=('Helvetica', 10), bg="gray", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(frame, text="Click INSERT to continue", font=('Helvetica', 10), bg="gray", fg="white")
    sk.grid(row=2, sticky=W)
    b = Button(frame, text="INSERT", command=lambda :file_opener(), width=20, fg='gray15', bg='snow',font=('Helvetica',10,'bold'), bd=0)
    b.grid(row=3,  pady=5)

    frame1 = LabelFrame(window, padx=20, pady=20, bg="gray", fg="pink", bd=0)
    frame1.grid(row=0, column=1, padx=5, pady=5)
    sk1 = Label(frame1, text="SECOND PDF", font=('Helvetica', 15, 'bold'), bg="gray", fg="white", borderwidth=1, relief='raised')
    sk1.grid(row=0, sticky=W + E)
    sk1 = Label(frame1, text="Insert The Second PDF ", font=('Helvetica', 10), bg="gray", fg="white")
    sk1.grid(row=1, sticky=W, pady=5)
    sk1 = Label(frame1, text="Click INSERT to continue", font=('Helvetica', 10), bg="gray", fg="white")
    sk1.grid(row=2, sticky=W)
    b1= Button(frame1, text="INSERT",command=lambda :file_opener(),width=20, fg='gray15', bg='snow', font=('Helvetica', 10, 'bold'), bd=0)
    b1.grid(row=3, pady=5)

    frame2 = LabelFrame(windoww,padx=0,pady=20,bg="gray",fg="pink",bd=0)
    frame2.grid(row=2, padx=0, pady=0)
    b2=Button(frame2,text="Merge",command=lambda:file_merger(),width=20,fg='black',bg='pink',font=("Helvetica",10,'bold'),bd=0)
    b2.grid(row=0,pady=5)
    sen1=Label(frame2,text="Resultant merged file will have its destination in root directory",font=('Calibra',10,'bold'),bg='gray',fg="White")
    sen1.grid(row=1)


main_window()
mainloop()