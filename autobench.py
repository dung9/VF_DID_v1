import cv2,os
import time
import numpy as np
from pyaxidraw import axidraw   # import module
mm_to_pex = 0.2645833333
Pex_x = 1920
Pex_y = 1080
class ADBAuto():
    def __init__(self,emulator):
        self.emulator = emulator
    def screen_capture(self,name):
        os.system(f'adb -s {self.emulator} exec-out screencap -p > {name}.png')

    def click(self,x,y):
        os.system(f'adb -s {self.emulator} shell input tap {x} {y}')

    def find_template(self,target_pic_name='', template_pic_name = False,threshold = 0.99):
        if template_pic_name == False:
            self.screen_capture(self.emulator)
            template_pic_name = self.emulator + '.png'
        else:
            self.screen_capture(template_pic_name)

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
            self.screen_capture(self.emulator)
            template_pic_name = self.emulator + '.png'
        else:
            self.screen_capture(template_pic_name)
        return is_match, point,test_data
OpenHeat = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heating_Pass.png'
Heat_Lv1 = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heat_level1.png'
Heat_Lv2 = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heat_level2.png'
Heat_Lv3 = 'C:/Users/FLASH/Downloads/ECU_Script/Image/Heat_level3.png'
Heatcheck = [OpenHeat,Heat_Lv1,Heat_Lv2,Heat_Lv3]
d = ADBAuto('MHU532019')
for j in range(2):
    time.sleep(5)
    for i in range(4):
        is_match, point,test_data = d.find_template(target_pic_name=Heatcheck[i])
        print(is_match, point,test_data)
        x,y = test_data[0][0],test_data[0][1]
                    #d.click(x,y)
        print(x,y)
        print(x*mm_to_pex,y*mm_to_pex)

        ad = axidraw.AxiDraw()          # Initialize class
        ad.interactive()                # Enter interactive context
        if not ad.connect():            # Open serial port to AxiDraw;
            quit()                      #   Exit, if no connection.
        ad.options.model = 2
        ad.options.accel = 80
        ad.options.units = 2        # set working units to mm.
        ad.update()                                  # Absolute moves follow:
        ad.moveto((x*mm_to_pex)/1.415, (y*mm_to_pex)/1.415)                 # Pen-up move to (1 inch, 1 inch)
        ad.lineto((x*mm_to_pex)/1.415, (y*mm_to_pex)/1.415)                 # Pen-down move, to (2 inch, 1 inch)
        ad.moveto(0, 0)                 # Pen-up move, back to origin.
ad.disconnect()
