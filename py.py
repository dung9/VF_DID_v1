# Import Module
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import cantools
 
# Create Tkinter Object
root = Tk()
root.geometry("700x300")
# Read the Image
image =  Image.open("Disconnect.png")
image1 = Image.open("Connect.png")
image2 = Image.open("dots.png")
 
# Resize the image using resize() method
resize_image = image.resize((20,20))
resize_image1 = image1.resize((20,20))
resize_image2 = image2.resize((20,20))

Disconnect = ImageTk.PhotoImage(resize_image)
Connect = ImageTk.PhotoImage(resize_image1) 
Dot3 = ImageTk.PhotoImage(resize_image2)

def Infor():
    filetypes = (
        ('text files', '*.dbc'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )
    db = cantools.database.load_file(filename)
    Infor_DBC.config(text=filename)
def Body():
    filetypes = (
        ('text files', '*.dbc'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )
    db = cantools.database.load_file(filename)
    Body_DBC.config(text=filename)
def PT():
    filetypes = (
        ('text files', '*.dbc'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )
    db = cantools.database.load_file(filename)
    PT_DBC.config(text=filename)
def CH():
    filetypes = (
        ('text files', '*.dbc'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )
    db = cantools.database.load_file(filename)
    CH_DBC.config(text=filename)
def D():
    filetypes = (
        ('text files', '*.dbc'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )
    db = cantools.database.load_file(filename)
    D_DBC.config(text=filename)
def HV():
    filetypes = (
        ('text files', '*.dbc'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )
    db = cantools.database.load_file(filename)
    HV_DBC.config(text=filename)


Infor_Label= Label(root, text= "Infor Database", font= ('Helvetica 15 underline'))
Infor_Label.place(relx = 0.01, rely = 0.1)
Infor_DBC= Label(root,text='                                                   ', font= ('Helvetica 15 underline'),width= 30, height=1,foreground='black')
Infor_DBC.place(relx = 0.3, rely = 0.1)
Button1 = Button(image=Dot3,command = Infor)
Button1.image = Dot3
Button1.place(relx = 0.85, rely = 0.1)
Connect1 = Label(image=Disconnect)
Connect1.image = Disconnect
Connect1.place(relx = 0.9, rely = 0.1)

Body_Label= Label(root, text= "Body Database", font= ('Helvetica 15 underline'))
Body_Label.place(relx = 0.01, rely = 0.2)
Body_DBC= Label(root,text='                                                     ', font= ('Helvetica 15 underline'),width= 30, height=1,foreground='black')
Body_DBC.place(relx = 0.3, rely = 0.2)
Button2 = Button(image=Dot3,command = Body)
Button2.image = Dot3
Button2.place(relx = 0.85, rely = 0.2)
Connect2 = Label(image=Disconnect)
Connect2.image = Disconnect
Connect2.place(relx = 0.9, rely = 0.2)

PT_Label= Label(root, text= "Powertrain Database", font= ('Helvetica 15 underline'))
PT_Label.place(relx = 0.01, rely = 0.3)
PT_DBC= Label(root,text='                                                        ', font= ('Helvetica 15 underline'),width= 30, height=1,foreground='black')
PT_DBC.place(relx = 0.30, rely = 0.3)
Button3 = Button(image=Dot3,command = PT)
Button3.image = Dot3
Button3.place(relx = 0.85, rely = 0.3)
Connect3 = Label(image=Disconnect)
Connect3.image = Disconnect
Connect3.place(relx = 0.9, rely = 0.3)

CH_Label= Label(root, text= "Chassis Database", font= ('Helvetica 15 underline'))
CH_Label.place(relx = 0.01, rely = 0.4)
CH_DBC= Label(root,text='                                                        ', font= ('Helvetica 15 underline'),width= 30, height=1,foreground='black')
CH_DBC.place(relx = 0.30, rely = 0.4)
Button4 = Button(image=Dot3,command = CH)
Button4.image = Dot3
Button4.place(relx = 0.85, rely = 0.4)
Connect4 = Label(image=Disconnect)
Connect4.image = Disconnect
Connect4.place(relx = 0.9, rely = 0.4)

D_Label= Label(root, text= "Diagnostic Database", font= ('Helvetica 15 underline'))
D_Label.place(relx = 0.01, rely = 0.5)
D_DBC= Label(root,text='                                                         ', font= ('Helvetica 15 underline'),width= 30, height=1,foreground='black')
D_DBC.place(relx = 0.30, rely = 0.5)
Button5 = Button(image=Dot3,command = D)
Button5.image = Dot3
Button5.place(relx = 0.85, rely = 0.5)
Connect5 = Label(image=Disconnect)
Connect5.image = Disconnect
Connect5.place(relx = 0.9, rely = 0.5)

HV_Label= Label(root, text= "HV Can Database", font= ('Helvetica 15 underline'))
HV_Label.place(relx = 0.01, rely = 0.6)
HV_DBC= Label(root,text='                                                         ', font= ('Helvetica 15 underline'),width= 30, height=1,foreground='black')
HV_DBC.place(relx = 0.30, rely = 0.6)
Button6 = Button(image=Dot3,command = HV)
Button6.image = Dot3
Button6.place(relx = 0.8, rely = 0.6)
Connect6 = Label(image=Disconnect)
Connect6.image = Disconnect
Connect6.place(relx = 0.95, rely = 0.6)

def connect():
    Connect1.config(image=Connect)
    Connect2.config(image=Connect)
    Connect3.config(image=Connect)
    Connect4.config(image=Connect)
    Connect5.config(image=Connect)
    Connect6.config(image=Connect)


Channel_Connect = Button(text= 'Connect',command=connect)
Channel_Connect.place(relx=0.45,rely=0.8)

#======================================Read DID===========================================
root.mainloop()