import re
import threading
import multiprocessing
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

Excel_frame = tk.LabelFrame(root,bg = '#c3c3c3',text= 'Trace',borderwidth=1,relief='solid')
Excel_frame.pack(side=tk.RIGHT,padx=1,pady=1)
Excel_frame.pack_propagate(False)
Excel_frame.configure(width=1400,height=800)

Header = ["Name","ID","Data","Dir","Chn","Sender Node"]
style = ttk.Style()
style.theme_use('clam')
tree = ttk.Treeview(Excel_frame, column=("c1", "c2","c3","c4","c5","c6"), show='headings')
tree.pack(expand=True, fill='x')

tree.column("# "+ str(1), anchor='w',width=200)
tree.heading("# "+ str(1), text=Header[0])

tree.column("# "+ str(2), anchor='w',width=80)
tree.heading("# "+ str(2), text=Header[1])

tree.column("# "+ str(3), anchor='w',width=150)
tree.heading("# "+ str(3), text=Header[2])

tree.column("# "+ str(4), anchor='w',width=50)
tree.heading("# "+ str(4), text=Header[3])

tree.column("# "+ str(5), anchor='w',width=50)
tree.heading("# "+ str(5), text=Header[4])

tree.column("# "+ str(6), anchor='w',width=50)
tree.heading("# "+ str(6), text=Header[5])
tree.pack(expand=True, fill='y')
    
queue_ID = Queue(maxsize = 300000000)
queue_Data = Queue(maxsize = 300000000)
ID_Mess = [0 for i in range(10000)]
Mess_Index = IntVar()
Database_Import = IntVar()
data = [0 for i in range(10000)]
Mess_store = [[0 for i in range(30)] for i in range(100)]
def En_queue():
    check = 1
    global bus
    global Receive
    Receive = 0
    try:
        bus = can.interface.Bus(bustype='vector', app_name='VINFAST', channel= 0, bitrate=500000)
    except can.CanError:
        print("Reconnect Cancase")
    while True:                  
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
        
def Trace():
    Run = 0
    global index
    index = 0
    Mess_Name = ''
    Sender_Node = ''
    db = cantools.database.load_file('C:/Users/FLASH/Downloads/Python (1)/Python/15_Body_CAN_Matrix_V11.3.2.dbc')
    while True:
            exist = 0
            data_rev = ''
            if queue_ID.empty() == False:
                mess = queue_ID.get()
                DLC = queue_Data.get()
                for i in range(1000):
                    try:
                        if (str(mess) in str(db.messages[i].frame_id)) == True:
                            Mess_Name = str(db.messages[i].name)
                            Sender_Node = db.messages[i].senders
                            break
                    except IndexError:
                        break
                for i in range(DLC):
                    data[i] = queue_Data.get()

                for i in range(DLC):
                    data_rev = data_rev + str(hex(data[i])[2:].zfill(2)) + " " 
                if index == 0:
                    clear()
                    tree.insert('', 'end',iid =str(mess),values=(Mess_Name,str(hex(mess)),data_rev,"Rx",str(bus.channel_info)[20:],str(Sender_Node)))
                    tree.update()
                    tree.pack()
                    ID_Mess[index] = mess
                    Mess_store[index][0] = mess
                    Mess_store[index][1] = DLC
                    for i in range(DLC):
                        Mess_store[index][i+2] = data[i]
                    index +=1  
                for j in range(index):
                    if mess == ID_Mess[j]:
                        tree.item(str(mess),values=(Mess_Name,str(hex(mess)),data_rev,"Rx",str(bus.channel_info)[20:],str(Sender_Node)))
                        for n in range(index):
                            if Mess_store[n][0] == mess:
                                for i in range(DLC):
                                    Mess_store[n][i+2] = data[i]                                
                        exist = 1
                if index == 0 or exist == 0:
                    tree.insert('', 'end',iid =str(mess),values=(Mess_Name,str(hex(mess)),data_rev,"Rx",str(bus.channel_info)[20:],str(Sender_Node)))
                    tree.update()
                    tree.pack()
                    ID_Mess[index] = mess
                    Mess_store[index][0] = mess
                    Mess_store[index][1] = DLC
                    for i in range(DLC):
                        Mess_store[index][i+2] = data[i]
                    index +=1  
                Mess_Index.set(index)

def Database_define():
    db = cantools.database.load_file('C:/Users/FLASH/Downloads/Python (1)/Python/15_Body_CAN_Matrix_V11.3.2.dbc')  
    while True:
        if Mess_Index.get() > 0:
            for a in range(Mess_Index.get()):
                data = ''
                dataActual = '' 
                for k in range(Mess_store[a][1]):
                    data = data + str(bin(Mess_store[a][Mess_store[a][1] + 1 - k]))[2:].zfill(8)
                for kk in range(len(data)):
                    dataActual = dataActual + data[len(data)-1-kk]

                for iii in range(1000):
                    try:
                        if db.messages[iii].frame_id == Mess_store[a][0]:
                            for j in range(30):
                                try:
                                    data1 = ''
                                    value =''
                                    signal = str(db.messages[iii].signals[j])
                                    enbit = signal[signal.find(','):signal.find(',') + 5]
                                    leng = signal[signal.find(',') + 5:signal.find(',') + 10]
                                        
                                    m1 = re.sub(r'\D','', enbit)
                                    m2 = re.sub(r'\D','', leng)
                                    for k in range(int(m2)):
                                            data1 = data1 + dataActual[int(m1)-int(m2)+1+k]
                                    for v in range(len(data1)):
                                        value = value + data1[len(data1)-1-v]      

                                    Symbol_Value = signal[signal.find(', {')+3:signal.find('}')]
                                    Valuerow = ''
                                    for cout in range(20):
                                        if (str(int(value,2)) in Symbol_Value) == True:
                                            if Symbol_Value[Symbol_Value.find("'",Symbol_Value.find(str(int(value,2)))) + 1 + cout] == "'":
                                                break
                                            Valuerow = Valuerow + Symbol_Value[Symbol_Value.find("'",Symbol_Value.find(str(int(value,2)))) + cout + 1]    
                                        else:
                                            break   

                                    #print(str(db.messages[iii].signals[j].name) + '    ' + str(int(value,2)) + '    ' + str(Valuerow))
                                    if Mess_store[a][19] == 0:
                                        tree.insert(str(Mess_store[a][0]), 'end',iid =str(db.messages[iii].signals[j].name),values=('     ' + str(db.messages[iii].signals[j].name), str(int(value,2)),str(Valuerow),'',''),open=False)
                                        tree.update() 
                                    elif Mess_store[a][19] == 1:
                                        tree.item(str(db.messages[iii].signals[j].name),values=(tree.item(str(db.messages[iii].signals[j].name))["values"][0],str(int(value,2)),str(Valuerow),'',''))                 
                                except IndexError:
                                    break
                            Mess_store[a][19] = 1
                    except IndexError:
                        break
def clear():
    tree.delete(*tree.get_children())
    tree.update()
    
if __name__ == '__main__':
    threading.Thread(target=Trace).start()    
    threading.Thread(target=En_queue).start()
    threading.Thread(target=Database_define).start()
root.mainloop()