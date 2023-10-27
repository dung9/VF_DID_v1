from tkinter import *
from tkinter.ttk import *
import can
import subprocess
try:
    bus = can.interface.Bus(bustype='vector', app_name='VINFAST', channel= 1, bitrate=500000)
    print('Connect with can box is done')
except can.CanError:
    print('Check can box is connect or not')
#BCM DTC
BCM_DiagRq_DTC = can.Message(arbitration_id= 0x681,
                 is_extended_id= 0,
                 dlc= 8,data=[3, 25, 2, 9, 255, 255, 255, 255],
                 check = False)
BCM_DiagRq_DTC1 = can.Message(arbitration_id= 0x681,
                 is_extended_id= 0,
                 dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                 check = False)

def ECU_Req_INFOR(message):
    try:
        bus.send(message)
    except can.CanError:
        print("Msg cannot send")

def ECU_Resp(ECU_ID):
    global ECU_LIST
    ECU_LIST = [0 for i in range(200)]
    count = 0 
    DTC_STATUS = 0
    #while DTC_STATUS == 0:
    mess = bus.recv(timeout = 2)
    try:
        if mess.arbitration_id == ECU_ID:
            if mess.data[0] == 16:
                ECU_Req_INFOR(BCM_DiagRq_DTC1)
            for i in range(7):
                ECU_LIST[count] = mess.data[i]
                count +=1
    except AttributeError:
        print('Can not read DTC')
        DTC_STATUS = 1
ECU_Req_INFOR(BCM_DiagRq_DTC)
ECU_Resp(0x601)
print(ECU_LIST)