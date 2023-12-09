import can
import can.interfaces.vector
import time
import threading
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Button, Entry, IntVar, ttk
from tkinter import IntVar
import nidaqmx
import nidaqmx.system
import time
__all__ = ['errors', 'scale', 'stream_readers', 'stream_writers', 'task']

root = tk.Tk()
root.title('Treeview Demo - Hierarchical Data')
root.geometry('200x100')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
Can_Mess = IntVar()
Daq_Init = IntVar()
Daq_Init.set(0)
Can_Mess.set(0)
CRCtable =[
            0x00, 0x1D, 0x3A, 0x27, 0x74, 0x69, 0x4E, 0x53,
            0xE8, 0xF5, 0xD2, 0xCF, 0x9C, 0x81, 0xA6, 0xBB,
            0xCD, 0xD0, 0xF7, 0xEA, 0xB9, 0xA4, 0x83, 0x9E,
            0x25, 0x38, 0x1F, 0x02, 0x51, 0x4C, 0x6B, 0x76,
            0x87, 0x9A, 0xBD, 0xA0, 0xF3, 0xEE, 0xC9, 0xD4,
            0x6F, 0x72, 0x55, 0x48, 0x1B, 0x06, 0x21, 0x3C,
            0x4A, 0x57, 0x70, 0x6D, 0x3E, 0x23, 0x04, 0x19,
            0xA2, 0xBF, 0x98, 0x85, 0xD6, 0xCB, 0xEC, 0xF1,
            0x13, 0x0E, 0x29, 0x34, 0x67, 0x7A, 0x5D, 0x40,
            0xFB, 0xE6, 0xC1, 0xDC, 0x8F, 0x92, 0xB5, 0xA8,
            0xDE, 0xC3, 0xE4, 0xF9, 0xAA, 0xB7, 0x90, 0x8D,
            0x36, 0x2B, 0x0C, 0x11, 0x42, 0x5F, 0x78, 0x65,
            0x94, 0x89, 0xAE, 0xB3, 0xE0, 0xFD, 0xDA, 0xC7,
            0x7C, 0x61, 0x46, 0x5B, 0x08, 0x15, 0x32, 0x2F,
            0x59, 0x44, 0x63, 0x7E, 0x2D, 0x30, 0x17, 0x0A,
            0xB1, 0xAC, 0x8B, 0x96, 0xC5, 0xD8, 0xFF, 0xE2,
            0x26, 0x3B, 0x1C, 0x01, 0x52, 0x4F, 0x68, 0x75,
            0xCE, 0xD3, 0xF4, 0xE9, 0xBA, 0xA7, 0x80, 0x9D,
            0xEB, 0xF6, 0xD1, 0xCC, 0x9F, 0x82, 0xA5, 0xB8,
            0x03, 0x1E, 0x39, 0x24, 0x77, 0x6A, 0x4D, 0x50,
            0xA1, 0xBC, 0x9B, 0x86, 0xD5, 0xC8, 0xEF, 0xF2,
            0x49, 0x54, 0x73, 0x6E, 0x3D, 0x20, 0x07, 0x1A,
            0x6C, 0x71, 0x56, 0x4B, 0x18, 0x05, 0x22, 0x3F,
            0x84, 0x99, 0xBE, 0xA3, 0xF0, 0xED, 0xCA, 0xD7,
            0x35, 0x28, 0x0F, 0x12, 0x41, 0x5C, 0x7B, 0x66,
            0xDD, 0xC0, 0xE7, 0xFA, 0xA9, 0xB4, 0x93, 0x8E,
            0xF8, 0xE5, 0xC2, 0xDF, 0x8C, 0x91, 0xB6, 0xAB,
            0x10, 0x0D, 0x2A, 0x37, 0x64, 0x79, 0x5E, 0x43,
            0xB2, 0xAF, 0x88, 0x95, 0xC6, 0xDB, 0xFC, 0xE1,
            0x5A, 0x47, 0x60, 0x7D, 0x2E, 0x33, 0x14, 0x09,
            0x7F, 0x62, 0x45, 0x58, 0x0B, 0x16, 0x31, 0x2C,
            0x97, 0x8A, 0xAD, 0xB0, 0xE3, 0xFE, 0xD9, 0xC4]
Device = Entry(root)
Device.pack(padx=0,pady=0)

def calc_CRC(len,pos,data = [0 for i in range(8)]):
    crc = 0xff
    for i in range(len):
        if i != pos:
            crc = CRCtable[crc ^ data[i]]
    crc ^= 0xff
    return crc

def Ni_DAQ():
    system = nidaqmx.system.System.local()
    system.driver_version
    for device in system.devices:
        name = str(device)
    print(str(device))
    name = name[name.find("=") + 1:name.find(")")]
    Device.insert(0,name)
    Init = 0
    while True:
        
        if Can_Mess.get() == 1 and Init == 0:
            task = nidaqmx.Task()
            task.do_channels.add_do_chan(str(Device.get())+'/port0/line0:7')
            task.start()
            Init = 1
        if Daq_Init.get() == 1 and Init == 1:
            task.write([255,255,255,255,255,255,255,255])
        if Daq_Init.get() == 2:
            task.write([0,0,0,0,0,0,0,0])

def BCM_Clamp_STAT():
    
    BCM_Clamp_STAT = can.Message(arbitration_id= 0x112,
                                is_extended_id= False,dlc= 8,
                                data=[0, 0, 0, 85, 10, 0, 0, 0],
                                check = False)
    data = [0 for i in range(8)]

    while True:
        if Can_Mess.get() == 1:
            Bin_data1 = str(bin(BCM_Clamp_STAT.data[1]))[2:].zfill(8)
            Value_Alive = Bin_data1[4] + Bin_data1[5] +Bin_data1[6] + Bin_data1[7]
            if int(Value_Alive,2) < 14:
                BCM_Clamp_STAT.data[1] = BCM_Clamp_STAT.data[1] + 1
            else:    
                BCM_Clamp_STAT.data[1] = int(Bin_data1[0] + Bin_data1[1] +Bin_data1[2] + Bin_data1[3] + '0' + '0' + '0' + '0',2)
            for i in range(8):
                data[i] = BCM_Clamp_STAT.data[i]

            data[0] = calc_CRC(8,0,data)
            BCM_Clamp_STAT.data[0] = data[0]
            bus.send(BCM_Clamp_STAT)
            time.sleep(0.1)

def VCU_HV_DrvSys_status():
    VCU_HV_DrvSys = can.Message(arbitration_id= 0xD9,
                                is_extended_id= False,dlc= 8,
                                data=[0, 0, 0, 0, 0, 0, 0, 0],
                                check = False)
    data = [0 for i in range(8)]
    while True:
        if Can_Mess.get() == 1:
            Bin_data1 = str(bin(VCU_HV_DrvSys.data[1]))[2:].zfill(8)
            Value_Alive = Bin_data1[4] + Bin_data1[5] +Bin_data1[6] + Bin_data1[7]
            if int(Value_Alive,2) < 14:
                VCU_HV_DrvSys.data[1] = VCU_HV_DrvSys.data[1] + 1
            else:    
                VCU_HV_DrvSys.data[1] = int(Bin_data1[0] + Bin_data1[1] +Bin_data1[2] + Bin_data1[3] + '0' + '0' + '0' + '0',2)
            for i in range(8):
                data[i] = VCU_HV_DrvSys.data[i]

            data[0] = calc_CRC(8,0,data)
            VCU_HV_DrvSys.data[0] = data[0]
            bus.send(VCU_HV_DrvSys)
            time.sleep(0.015)
def connect_Can():
    global bus
    try:
        bus = can.interface.Bus(bustype='vector', app_name='VINFAST', channel= 0, bitrate=500000)
        Can_Mess.set(1)
        Daq_Init.set(1)
        print('Connect with can box is done')
    except can.CanError:
        print('Check can box is connect or not')
        Can_Mess.set(0)
def Disconnect_Daq():
    Can_Mess.set(0)
    Daq_Init.set(2)

Connect_bt = Button(root,text='Connect',command = connect_Can)
Disconnect_bt = Button(root,text='Disconnect',command = Disconnect_Daq)
Connect_bt.pack(padx=1,pady=1)
Disconnect_bt.pack(padx=1,pady=2)
if __name__ == '__main__':     
    threading.Thread(target=BCM_Clamp_STAT).start() 
    threading.Thread(target=VCU_HV_DrvSys_status).start()  
    threading.Thread(target=Ni_DAQ).start() 
root.mainloop()
