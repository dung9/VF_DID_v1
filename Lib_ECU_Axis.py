Home = 'C:/Users/FLASH/Downloads/ECU_Script/Image/menu.png'
OpenHeat = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heating_Pass.png'
OpenHeat1 = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heat_Pass1.png'
Heat_Lv1 = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heat_level1.png'
Heat_Lv1_Actual = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heat_level1_actual.png'
Heat_Lv2 = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heat_level2.png'
Heat_Lv3 = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heat_level3.png'
Home = 'C:/Users/FLASH/Downloads/ECU_Script/Image/menu.png'
def __init__(device):
    return device
def screen_capture(device):
    import os
    os.system(f'adb -s {device} exec-out screencap -p > {device}.png')

def find_template(device,target_pic_name ='', template_pic_name = False,threshold = 0.99):
    import cv2
    import numpy as np
    if template_pic_name == False:
        screen_capture(device)
        template_pic_name = device + '.png'
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
    if template_pic_name == False:
        screen_capture(device)
        template_pic_name = device
    else:
        screen_capture(device)
    return is_match, point,test_data

def Scan_Image(device,Image):
    is_match, point,test_data = find_template(__init__(device),target_pic_name = Image)
    #print(is_match, point,test_data)
    x,y = test_data[0][0],test_data[0][1]
    print(x,y)
    #print(x*mm_to_pex,y*mm_to_pex)
    return x,y

def moveto(device,Image):
    from pyaxidraw import axidraw   # import module
    mm_to_pex = 0.2645833333
    ad = axidraw.AxiDraw()          # Initialize class
    ad.interactive()                # Enter interactive context
    if not ad.connect():            # Open serial port to AxiDraw;
        quit()

    x,y = Scan_Image(device,Image)

    ad.options.model = 2
    ad.options.accel = 80
    ad.options.units = 2        # set working units to mm.
    ad.update()                                  # Absolute moves follow:
    ad.moveto((x*mm_to_pex)/1.415, (y*mm_to_pex)/1.415)                 # Pen-up move to (1 inch, 1 inch)
    ad.lineto((x*mm_to_pex)/1.415, (y*mm_to_pex)/1.415)                 # Pen-down move, to (2 inch, 1 inch)
    ad.moveto(0, 0)                 # Pen-up move, back to origin.
    ad.disconnect()

# moveto('MHU532019',OpenHeat)
# moveto('MHU532019',Heat_Lv1)
# moveto('MHU532019',Heat_Lv2)
# moveto('MHU532019',Heat_Lv3)
moveto('MHU532019',OpenHeat)
moveto('MHU532019',Heat_Lv1)
moveto('MHU532019',Heat_Lv2)
moveto('MHU532019',Heat_Lv3)
#screen_capture('MHU532019')