import threading
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Button, IntVar, ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
import can
import tkinter as tk
from threading import Thread
from queue import Queue 
import time
import cantools
root = tk.Tk()
root.title('Treeview Demo - Hierarchical Data')
root.geometry('800x500')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

Excel_frame = tk.LabelFrame(root,bg = '#c3c3c3',text= 'ECU Infor',borderwidth=1,relief='solid')
Excel_frame.pack(side=tk.TOP,padx=1,pady=1)
Excel_frame.pack_propagate(False)
Excel_frame.configure(width=1400,height=400)

Header = ["ID","Data","Chn","Dir"]
style = ttk.Style()
style.theme_use('clam')
tree = ttk.Treeview(Excel_frame, column=("c1", "c2","c3","c4"), show='headings')
tree.pack(expand=True, fill='x')
count = 0
for i in range(4):
    count += 1
    tree.column("# "+ str(count), anchor=CENTER,width=300)
    tree.heading("# "+ str(count), text=Header[i])
    tree.pack(expand=True, fill='y')
    
queue_ID = Queue(maxsize = 300000000)
queue_Data = Queue(maxsize = 300000000)
Run_Trace = IntVar()
# configure the grid layout
# create a treeview
def En_queue():
    check = 1
    global Receive
    Receive = 0
    try:
        bus = can.interface.Bus(bustype='vector', app_name='VINFAST', channel= 0, bitrate=500000)
    except can.CanError:
        print("Reconnect Cancase")
    while check == 1:                  
        mess = bus.recv()
        try:
            Receive = 0
            queue_ID.put(mess.arbitration_id)
            queue_Data.put(mess.dlc)
            for i in range(mess.dlc):     
                queue_Data.put(mess.data[i])
        except AttributeError:
            Receive = 1
            print("Not receive message")
            clear()
            while queue_ID.empty() == False:
                queue_ID.get()
            while queue_Data.empty() == False:
                queue_Data.get()   
        
def Trace():
    Run = 0
    data = [0 for i in range(10000)]
    global index
    index = 0
    ID_Mess = [0 for i in range(10000)]
    while Run == 0:
            exist = 0
            data_rev = ''
            if Receive == 1:
                ID_Mess = [0 for i in range(10000)]
                index = 0
            if queue_ID.empty() == False:
                mess = queue_ID.get()
                DLC = queue_Data.get()

                for i in range(DLC):
                    data[i] = queue_Data.get()

                for i in range(DLC):
                    data_rev = data_rev + str(hex(data[i])[2:].zfill(2)) + " " 

                if index == 0 :
                    tree.insert('', 'end',iid =str(mess),values=(str(hex(mess)),data_rev,"Discription","None"))
                    tree.pack()
                    ID_Mess[index] = mess
                    index +=1
                for j in range(index):
                    if mess == ID_Mess[j]:
                        tree.item(str(mess),values=(str(hex(mess)),data_rev,"Discription","None"))
                        exist = 1
                if exist == 0:
                        tree.insert('', 'end',iid =str(mess),values=(str(hex(mess)),data_rev,"Discription","None"))
                        tree.pack()
                        ID_Mess[index] = mess
                        index +=1  
    #if str(queue[0]) in tree.item(ECU_LIST[j])["values"]
def clear():
        time.sleep(10)
        tree.delete(*tree.get_children())
        tree.update()
if __name__ == '__main__':
    t1 = threading.Thread(target=En_queue, name="t1")
    t2 = threading.Thread(target=Trace, name="t2")

    t1.start()
    t2.start()
    #Thread(target = clear).start()
root.mainloop()