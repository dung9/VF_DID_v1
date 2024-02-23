def Capture_Image(WebCam_Index,Name):
    import cv2
    cam_port = WebCam_Index
    cam = cv2.VideoCapture(cam_port) 
    result, image = cam.read() 
    if result: 
        cv2.imshow("Wedcam" + Name, image)
        cv2.imwrite("Wedcam" + Name, image)
        cv2.waitKey(0) 
        cv2.destroyWindow("GeeksForGeeks")  
    else: 
        print("No image detected. Please! try again") 

def Test():
    return 'Run'

def __init__(device):
    return device

def screen_capture(device):
    import os
    os.system(f'adb -s {device} exec-out screencap -p > C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Templete_Image.png')
def click(device,x,y):
    import os
    os.system(f'adb -s {device} shell input tap {x} {y}')
def find_template(device,target_pic_name ='',template_pic_name = False,threshold = 0.95):
    import cv2
    import numpy as np
    if template_pic_name == False:
        screen_capture(device)
        template_pic_name = 'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Templete_Image.png'
    else:
        screen_capture(device)
    img = cv2.imread(target_pic_name)
    img2 = cv2.imread(template_pic_name)
    w = img2.shape[1]
    h = img2.shape[0]
    result = cv2.matchTemplate(img,img2, cv2.TM_CCOEFF_NORMED)
    loc =  np.where( result >= threshold)
    test_data = list(zip(*loc[::-1]))
    is_match = len(test_data) > 0
    point= []
    if is_match:
        point.append((test_data[0][0] + w/2, test_data[0][1] + h/2))
        print("Image is avaible")
        return test_data
    else:
        print("Image is not avaible")
        return False
def Change_Temp(target_pic_name ='',threshold = 0.95):
    import cv2
    import numpy as np
    template_pic_name = 'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/CCU_CLIMATE_CONTROL/Templete_Image_change_Temp.png'
    img = cv2.imread(target_pic_name)
    img2 = cv2.imread(template_pic_name)
    w = img2.shape[1]
    h = img2.shape[0]
    result = cv2.matchTemplate(img,img2, cv2.TM_CCOEFF_NORMED)
    loc =  np.where( result >= threshold)
    test_data = list(zip(*loc[::-1]))
    is_match = len(test_data) > 0
    point= []
    if is_match:
        point.append((test_data[0][0] + w/2, test_data[0][1] + h/2))
        print("Image is avaible")
        return test_data
    else:
        print("Image is not avaible")
        return False
def find_template_Temp(target_pic_name ='',template_pic_name ='',threshold = 0.95):
    import cv2
    import numpy as np
    img = cv2.imread(target_pic_name)
    img2 = cv2.imread(template_pic_name)
    w = img2.shape[1]
    h = img2.shape[0]
    result = cv2.matchTemplate(img,img2, cv2.TM_CCOEFF_NORMED)
    loc =  np.where( result >= threshold)
    test_data = list(zip(*loc[::-1]))
    is_match = len(test_data) > 0
    if is_match:
        return True
    else:
        return False
def Compare_image(device,target_pic_name ='',template_pic_name = False,threshold = 0.95):
    import cv2
    import numpy as np
    if template_pic_name == False:
        screen_capture(device)
        template_pic_name = 'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Templete_Image.png'
    else:
        screen_capture(device)
    img = cv2.imread(target_pic_name)
    img2 = cv2.imread(template_pic_name)
    result = cv2.matchTemplate(img,img2, cv2.TM_CCOEFF_NORMED)
    loc =  np.where( result >= threshold)
    test_data = list(zip(*loc[::-1]))
    is_match = len(test_data) > 0
    if is_match:
        print("Image is avaible")
        return True
    else:
        print("Image is not avaible")
        return False
def Scan_Image(device,Image):    
    try:
        test_data = find_template(__init__(device),target_pic_name = Image)
        x,y = test_data[0][0],test_data[0][1]
        return x,y
    except:
        return False
def Scan_Image_NotCapture(Image):    
    try:
        test_data = Change_Temp(target_pic_name = Image)
        x,y = test_data[0][0],test_data[0][1]
        return x,y
    except:
        return False
def Init_axis():
    from pyaxidraw import axidraw   # import module
    ad = axidraw.AxiDraw() 
    ad.interactive() 
    if not ad.connect():            # Open serial port to AxiDraw;
        quit()
    ad.options.model = 2
    ad.options.speed_penup = 300
    ad.options.speed_pendown = 300
    ad.options.units = 2        # set working units to mm.
    ad.update()
    return ad
def moveto(ad,device,Image,touch,s,Return):
    import time
    mm_to_pex = 0.2645833333    
    x,y = Scan_Image(device,Image)
    for i in range(touch):                            # Absolute moves follow:
        ad.moveto((x*mm_to_pex)/1.415, (y*mm_to_pex)/1.415)                 # Pen-up move to (1 inch, 1 inch)
        ad.lineto((x*mm_to_pex)/1.415, (y*mm_to_pex)/1.415)                 # Pen-down move, to (2 inch, 1 inch)
        ad.moveto((x*mm_to_pex)/1.415, (y*mm_to_pex)/1.415)                 # Pen-up move to (1 inch, 1 inch)        
        time.sleep(s)
    if Return == True:
        ad.moveto(0, 0)                 # Pen-up move, back to origin.
        ad.disconnect()
def moveto_NotCapture(ad,device,Image,touch,s,Return):
    import time
    mm_to_pex = 0.2645833335    
    x,y = Scan_Image_NotCapture(Image)
    for i in range(touch):                            # Absolute moves follow:
        ad.moveto((x*mm_to_pex)/1.417, (y*mm_to_pex)/1.417)                 # Pen-up move to (1 inch, 1 inch)
        ad.lineto((x*mm_to_pex)/1.417, (y*mm_to_pex)/1.417)                 # Pen-down move, to (2 inch, 1 inch)
        ad.moveto((x*mm_to_pex)/1.417, (y*mm_to_pex)/1.417)                 # Pen-up move to (1 inch, 1 inch)        
        time.sleep(s)
    if Return == True:
        ad.moveto(0, 0)                 # Pen-up move, back to origin.
        ad.disconnect()
def Return(ad):
    ad.moveto(0, 0)                 # Pen-up move, back to origin.
    ad.disconnect()

def moveto_xy(ad,x,y,touch,s):
    import time                             # Absolute moves follow:
    for i in range(touch):
        ad.moveto(x, y)              # Pen-up move to (1 inch, 1 inch)
        ad.lineto(x, y) 
        time.sleep(s)   
    ad.moveto(0, 0)                 # Pen-up move, back to origin.

def Check_Temp_Display():
    import subprocess
    subprocess.call(["C:\\Users\\FLASH\\ECU-TEST\\Workspace\\App\\dist\\Temp_Display.exe"])
def Check_FAN_Display():
    import subprocess
    subprocess.call(["C:\\Users\\FLASH\\ECU-TEST\\Workspace\\App\\dist\\FAN.exe"])

def Detect_image(Image,device):
    import numpy as np
    import cv2
    template = cv2.resize(cv2.imread(Image, 0), (0, 0), fx=1, fy=1)
    screen_capture(device)
    img = cv2.resize(cv2.imread('C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Templete_Image.png', 0), (0, 0), fx=1, fy=1)
    h, w = template.shape
    methods = [cv2.TM_CCOEFF_NORMED,  cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    Data_x = [0 for i in range(5)] 
    Data_y = [0 for i in range(5)] 
    i = 0
    Result = True
    for method in methods:
        img2 = img.copy()
        i = i+1
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc
        bottom_right = (location[0] + w, location[1] + h) 
        Data_x[i] = location[0] + w
        Data_y[i] = location[1] + h
        print(bottom_right)   
    if Data_x[1] == Data_x[2] and Data_x[2] == Data_x[3] and Data_x[3] == Data_x[4] and Data_y[1] == Data_y[2] and Data_y[2] == Data_y[3] and Data_y[3] == Data_y[4]:
        print('Maching')
        Result = True
        return Result
    else:
        print('Not Maching')
        Result = False
        return Result
def scroll_setting_content(device,option):
    import os
    if option == "up":
        os.system(f'adb -s {device} shell input swipe 1000 400 1000 700')
    elif option == "down":
        os.system(f'adb -s {device} shell input swipe 1000 700 1000 400')

def scroll_setting_option(device,option):
    import os
    if option == "up":
        os.system(f'adb -s {device} shell input swipe 700 400 700 800')
    elif option == "down":
        os.system(f'adb -s {device} shell input swipe 700 500 700 800')
def CanoeLog(Location,Status):
    import os
    from py_canoe import CANoe
    from time import sleep as wait
    canoe_inst = CANoe()
    canoe_inst.open(canoe_cfg = r"C:/Users/FLASH/Documents/ECU_Script/Canconfig/Can.cfg")
    if Status == "Start":
        Mylocation = str(Location)
        index1 = Mylocation.find('//')
        index2 = Mylocation.find('Images')
        Tescase_name = Mylocation[index1+2:index2-1]
        # print(Mylocation)
        index = Mylocation.find('Image')
        if index == -1:
            print ("Not found.")
        else:
            print ("Found at index", index)
        Mylocation = Mylocation[index+7:]    

        pythonfile = Mylocation

        for root, dirs, files in os.walk(r'C:/Users/FLASH/ECU-TEST/Workspace/TestReports'):
            for name in files:
                if name == pythonfile: 
                    Location_actual = os.path.abspath(os.path.join(root, name))
                    # print(Location_actual + Tescase_name)
        index = Location_actual.find('Image')
        Location_actual = Location_actual[:index]    
        Location_actual = Location_actual.replace(chr(92),'/')
        Location_actual = Location_actual + Tescase_name
        canoe_inst.start_measurement()
        wait(1)
        canoe_inst.set_system_variable_value('Log::Name',Location_actual)
        wait(1)
        canoe_inst.set_system_variable_value('Log::Getlog',1)


def Get_name(Location):
    Testcase_Location = str(Location)
    index1 = Testcase_Location.find('//')
    index2 = Testcase_Location.find('Images')
    Tescase_name = Testcase_Location[index1+2:index2-1]
    print(Tescase_name)
    return(Tescase_name)

def Log_Temp(LogPath,count,DATA1, DATA2,DATA3):
    import os
    from openpyxl import Workbook
    wb = Workbook()
    
    if count == 1:
        wb.create_sheet("Temp_Driver")
        
    data = wb["Temp_Driver"]
    data['A1'] = 'Temp display'
    data['B1'] = 'Temp CAN message from CCU'
    data['C1'] = 'Temp CAN message from MHU'
    data['A'+ str(count + 1)] = str(DATA1)
    data['B'+ str(count + 1)] = str(DATA2)
    data['C'+ str(count + 1)] = str(DATA3)
    Mylocation = str(LogPath)
    index = Mylocation.find('Image')
    Mylocation = Mylocation[index+7:]    
    pythonfile = Mylocation
    for root, dirs, files in os.walk(r'C:/Users/FLASH/ECU-TEST/Workspace/TestReports'):
        for name in files:
            if name == pythonfile: 
                Location_actual = os.path.abspath(os.path.join(root, name))
    index = Location_actual.find('Image') 
    Location_actual = Location_actual[:index]             
    Location_actual = Location_actual.replace(chr(92),'/')
    wb.save(Location_actual + "Log_Temp_Display.xlsx")
    count = count + 1
    return count
def Touch_Temp(data1,data2):
    Touch = abs((data1 - data2)/5)
    return int(Touch)
def Change_Pass(Pass_Name,ad,device):
    Char_Array = [0 for i in range(30)]
    Define_Char = "0123456789abcdefghijklmnopqrstuvwxyz"
    Char_Array = ['C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN0.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN1.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN2.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN3.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN4.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN5.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN6.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN7.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN8.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeN9.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Char_a.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Char_b.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Char_c.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Char_d.png',
                  'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Char_e.png']
    for i in range(len(Pass_Name)):
        index = Define_Char.find(Pass_Name[i])
        if Compare_image(device,Char_Array[index]) == True:
            moveto(ad,device,Char_Array[index],1,0,False)
        else:
            if  Compare_image(device,'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changecharactor.png') == True:
                moveto(ad,device,'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changecharactor.png',1,0,False)
                if Compare_image(device,Char_Array[index]) == True:
                    moveto(ad,device,Char_Array[index],1,0,False)
                else:
                    Return(ad)
                    break
            else:
                moveto(ad,device,'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Keyboard_changeNumber.png',1,0,False)
                if Compare_image(device,Char_Array[index]) == True:
                    moveto(ad,device,Char_Array[index],1,0,False)
                else:
                    Return(ad)
                    break  
    if  Compare_image(device,'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Change_Pass_Icon.png') == True:
        moveto(ad,device,'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Change_Pass_Icon.png',1,0,True)
    else:
        moveto(ad,device,'C:/Users/FLASH/ECU-TEST/Workspace/Images/Image_MHU/Wifi_Icon/Change_Pass_Icon_1.png',1,0,True)
    
def Eye_Image_Location(Location):
    import os
    Mylocation = str(Location)
    index1 = Mylocation.find('Images')
    index2 = Mylocation.find('png')
    Mylocation=Mylocation[index1+7:index2+3]
    pythonfile = Mylocation
    for root, dirs, files in os.walk(r'C:/Users/FLASH/ECU-TEST/Workspace/TestReports'):
        for name in files:
            if name == pythonfile: 
                Location_actual = os.path.abspath(os.path.join(root, name))    
    Location_actual = Location_actual.replace(chr(92),'/')
    return Location_actual
def Compare_Without_Adb(device,target_pic_name ='',Eye_Image = False,threshold = 0.95):
    import cv2
    import numpy as np
    template_pic_name = Eye_Image
    img = cv2.imread(target_pic_name)
    img2 = cv2.imread(template_pic_name)
    result = cv2.matchTemplate(img,img2, cv2.TM_CCOEFF_NORMED)
    loc =  np.where( result >= threshold)
    test_data = list(zip(*loc[::-1]))
    is_match = len(test_data) > 0
    if is_match:
        print("Image is avaible")
        return True
    else:
        print("Image is not avaible")
        return False
    