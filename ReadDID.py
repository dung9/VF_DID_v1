from tkinter import *
from tkinter.ttk import *
import can
import subprocess
HW = 1
SW = 2
HW_rv = 3
bl = 4
#===========================Init Can Message================================
#=========================ACM===============================
ACM_DiagRq__PU = can.Message(arbitration_id= 0x688,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
ACM_DiagRq_PU_Rv = can.Message(arbitration_id=0x688,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
ACM_DiagRq_HW = can.Message(arbitration_id= 0x688,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
ACM_DiagRq_HW_Rv = can.Message(arbitration_id=0x688,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
ACM_DiagRq_SW = can.Message(arbitration_id= 0x688,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
ACM_DiagRq_SW_Rv = can.Message(arbitration_id= 0x688,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
ACM_DiagRq_CAL = can.Message(arbitration_id= 0x688,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
ACM_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x688,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
ACM_DiagRq_Bootloader = can.Message(arbitration_id= 0x688,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
ACM_DiagRq = can.Message(arbitration_id= 0x688,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================ACM===============================
ABS_DiagRq_HW = can.Message(arbitration_id= 0x6A9,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
ABS_DiagRq_HW_Rv = can.Message(arbitration_id=0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
ABS_DiagRq_SW = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
ABS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
ABS_DiagRq_CAL = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
ABS_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
ABS_DiagRq_Bootloader = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
ABS_DiagRq = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================EAC===============================
EAC_DiagRq_PU = can.Message(arbitration_id= 0x6F5,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
EAC_DiagRq_PU_Rv = can.Message(arbitration_id=0x6F5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
EAC_DiagRq_HW = can.Message(arbitration_id= 0x6F5,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
EAC_DiagRq_HW_Rv = can.Message(arbitration_id=0x6F5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
EAC_DiagRq_SW = can.Message(arbitration_id= 0x6F5,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
EAC_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6F5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
EAC_DiagRq_Bootloader = can.Message(arbitration_id= 0x6F5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
EAC_DiagRq = can.Message(arbitration_id= 0x6F5,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================APM===============================
APM_DiagRq_HW = can.Message(arbitration_id= 0x6C1,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
APM_DiagRq_HW_Rv = can.Message(arbitration_id=0x6C1,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
APM_DiagRq_SW = can.Message(arbitration_id= 0x6C1,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
APM_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6C1,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
APM_DiagRq_Bootloader = can.Message(arbitration_id= 0x6C1,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
APM_DiagRq = can.Message(arbitration_id= 0x6C1,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================AVAS===============================
AVAS_DiagRq_PU = can.Message(arbitration_id= 0x6AA,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
AVAS_DiagRq_PU_Rv = can.Message(arbitration_id=0x6AA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
AVAS_DiagRq_HW = can.Message(arbitration_id= 0x6AA,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
AVAS_DiagRq_HW_Rv = can.Message(arbitration_id=0x6AA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
AVAS_DiagRq_SW = can.Message(arbitration_id= 0x6AA,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
AVAS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6AA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
AVAS_DiagRq_Bootloader = can.Message(arbitration_id= 0x6AA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
AVAS_DiagRq = can.Message(arbitration_id= 0x6AA,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================BAS===============================
BAS_DiagRq_HW = can.Message(arbitration_id= 0x6D8,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
BAS_DiagRq_HW_Rv = can.Message(arbitration_id=0x6D8,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
BAS_DiagRq_SW = can.Message(arbitration_id= 0x6D8,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
BAS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6D8,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
BAS_DiagRq_Bootloader = can.Message(arbitration_id= 0x6D8,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
BAS_DiagRq = can.Message(arbitration_id= 0x6D8,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================BCM_BPM===============================
BCM_BPM_DiagRq_PU = can.Message(arbitration_id= 0x6FB,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
BCM_BPM_DiagRq_PU_Rv = can.Message(arbitration_id=0x6FB,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
BCM_BPM_DiagRq_HW = can.Message(arbitration_id= 0x6FB,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
BCM_BPM_DiagRq_HW_Rv = can.Message(arbitration_id=0x6FB,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
BCM_BPM_DiagRq_SW = can.Message(arbitration_id= 0x6FB,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
BCM_BPM_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6FB,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
BCM_BPM_DiagRq_Bootloader = can.Message(arbitration_id= 0x6FB,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
BCM_BPM_DiagRq = can.Message(arbitration_id= 0x6FB,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================BCM===============================
BCM_DiagRq_HW = can.Message(arbitration_id= 0x681,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
BCM_DiagRq_HW_Rv = can.Message(arbitration_id=0x681,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
BCM_DiagRq_SW = can.Message(arbitration_id= 0x681,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
BCM_DiagRq_SW_Rv = can.Message(arbitration_id= 0x681,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
BCM_DiagRq_Bootloader = can.Message(arbitration_id= 0x681,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
BCM_DiagRq = can.Message(arbitration_id= 0x681,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================BMS===============================
MS_DiagRq_PU = can.Message(arbitration_id= 0x693,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
BMS_DiagRq_PU_Rv = can.Message(arbitration_id=0x693,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
BMS_DiagRq_HW = can.Message(arbitration_id= 0x693,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
BMS_DiagRq_HW_Rv = can.Message(arbitration_id=0x693,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
BMS_DiagRq_SW = can.Message(arbitration_id= 0x693,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
BMS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x693,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
BMS_DiagRq_CAL = can.Message(arbitration_id= 0x693,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
BMS_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x693,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
BMS_DiagRq_Bootloader = can.Message(arbitration_id= 0x693,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
BMS_DiagRq = can.Message(arbitration_id= 0x693,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================LDM_L===============================
LDM_L_DiagRq_HW = can.Message(arbitration_id= 0x6C9,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
LDM_L_DiagRq_HW_Rv = can.Message(arbitration_id=0x6C9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
LDM_L_DiagRq_SW = can.Message(arbitration_id= 0x6C9,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
LDM_L_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6C9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
LDM_L_DiagRq_CAL = can.Message(arbitration_id= 0x6C9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
LDM_L_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6C9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
LDM_L_DiagRq_Bootloader = can.Message(arbitration_id= 0x6C9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
LDM_L_DiagRq = can.Message(arbitration_id= 0x6C9,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================LDM_R===============================
LDM_R_DiagRq_HW = can.Message(arbitration_id= 0x6CA,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
LDM_R_DiagRq_HW_Rv = can.Message(arbitration_id=0x6CA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
LDM_R_DiagRq_SW = can.Message(arbitration_id= 0x6CA,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
LDM_R_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6CA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
LDM_R_DiagRq_CAL = can.Message(arbitration_id= 0x6CA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
LDM_R_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6CA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
LDM_R_DiagRq_Bootloader = can.Message(arbitration_id= 0x6CA,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
LDM_R_DiagRq = can.Message(arbitration_id= 0x6CA,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================ASU===============================
ASU_DiagRq_HW = can.Message(arbitration_id= 0x691,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
ASU_DiagRq_HW_Rv = can.Message(arbitration_id=0x691,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
ASU_DiagRq_SW = can.Message(arbitration_id= 0x691,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
ASU_DiagRq_SW_Rv = can.Message(arbitration_id= 0x691,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
ASU_DiagRq_CAL = can.Message(arbitration_id= 0x691,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
ASU_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x691,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
ASU_DiagRq_Bootloader = can.Message(arbitration_id= 0x691,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
ASU_DiagRq = can.Message(arbitration_id= 0x691,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================CCUF===============================
CCUF_DiagRq_PU = can.Message(arbitration_id= 0x689,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
CCUF_DiagRq_PU_Rv = can.Message(arbitration_id=0x689,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
CCUF_DiagRq_HW = can.Message(arbitration_id= 0x689,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
CCUF_DiagRq_HW_Rv = can.Message(arbitration_id=0x689,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
CCUF_DiagRq_SW = can.Message(arbitration_id= 0x689,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
CCUF_DiagRq_SW_Rv = can.Message(arbitration_id= 0x689,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
CCUF_DiagRq_CAL = can.Message(arbitration_id= 0x689,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
CCUF_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x689,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
CCUF_DiagRq_Bootloader = can.Message(arbitration_id= 0x689,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
CCUF_DiagRq = can.Message(arbitration_id= 0x689,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================CCUR===============================
CCUR_DiagRq_HW = can.Message(arbitration_id= 0x694,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
CCUR_DiagRq_HW_Rv = can.Message(arbitration_id=0x694,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
CCUR_DiagRq_SW = can.Message(arbitration_id= 0x694,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
CCUR_DiagRq_SW_Rv = can.Message(arbitration_id= 0x694,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
CCUR_DiagRq_CAL = can.Message(arbitration_id= 0x694,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
CCUR_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x694,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
CCUR_DiagRq_Bootloader = can.Message(arbitration_id= 0x694,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
CCUR_DiagRq = can.Message(arbitration_id= 0x694,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================CPD===============================
CPD_DiagRq_HW = can.Message(arbitration_id= 0x6AF,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
CPD_DiagRq_HW_Rv = can.Message(arbitration_id=0x6AF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
CPD_DiagRq_SW = can.Message(arbitration_id= 0x6AF,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
CPD_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6AF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
CPD_DiagRq_Bootloader = can.Message(arbitration_id= 0x6AF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
CPD_DiagRq = can.Message(arbitration_id= 0x6AF,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================DIAG_Req===============================
DIAG_Req_DiagRq_HW = can.Message(arbitration_id= 0x6EF,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
DIAG_Req_DiagRq_HW_Rv = can.Message(arbitration_id=0x6EF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
DIAG_Req_DiagRq_SW = can.Message(arbitration_id= 0x6EF,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
DIAG_Req_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6EF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
DIAG_Req_DiagRq_Bootloader = can.Message(arbitration_id= 0x6EF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
DIAG_Req_DiagRq = can.Message(arbitration_id= 0x6EF,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================DIAG_Req===============================
DIAG_Req_DiagRq_HW = can.Message(arbitration_id= 0x6FF,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
DIAG_Req_DiagRq_HW_Rv = can.Message(arbitration_id=0x6FF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
DIAG_Req_DiagRq_SW = can.Message(arbitration_id= 0x6FF,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
DIAG_Req_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6FF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
DIAG_Req_DiagRq_Bootloader = can.Message(arbitration_id= 0x6FF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
DIAG_Req_DiagRq = can.Message(arbitration_id= 0x6FF,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================EDS_F===============================
EDS_F_DiagRq_HW = can.Message(arbitration_id= 0x69B,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
EDS_F_DiagRq_HW_Rv = can.Message(arbitration_id=0x69B,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
EDS_F_DiagRq_SW = can.Message(arbitration_id= 0x69B,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
EDS_F_DiagRq_SW_Rv = can.Message(arbitration_id= 0x69B,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
EDS_F_DiagRq_CAL = can.Message(arbitration_id= 0x69B,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
EDS_F_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x69B,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
EDS_F_DiagRq_Bootloader = can.Message(arbitration_id= 0x69B,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
EDS_F_DiagRq = can.Message(arbitration_id= 0x69B,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================EDS_R===============================
EDS_R_DiagRq_PU = can.Message(arbitration_id= 0x69A,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
EDS_R_DiagRq_PU_Rv = can.Message(arbitration_id=0x69A,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
EDS_R_DiagRq_HW = can.Message(arbitration_id= 0x69A,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
EDS_R_DiagRq_HW_Rv = can.Message(arbitration_id=0x69A,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
EDS_R_DiagRq_SW = can.Message(arbitration_id= 0x69A,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
EDS_R_DiagRq_SW_Rv = can.Message(arbitration_id= 0x69A,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
EDS_R_DiagRq_CAL = can.Message(arbitration_id= 0x69A,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
EDS_R_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x69A,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
EDS_R_DiagRq_Bootloader = can.Message(arbitration_id= 0x69A,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
EDS_R_DiagRq = can.Message(arbitration_id= 0x69A,
                           
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================EPS===============================
EPS_DiagRq_PU = can.Message(arbitration_id= 0x6A8,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
EPS_DiagRq_PU_Rv = can.Message(arbitration_id=0x6A8,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
EPS_DiagRq_HW = can.Message(arbitration_id= 0x6A8,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
EPS_DiagRq_HW_Rv = can.Message(arbitration_id=0x6A8,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
EPS_DiagRq_SW = can.Message(arbitration_id= 0x6A8,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
EPS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6A8,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
EPS_DiagRq_Bootloader = can.Message(arbitration_id= 0x6A8,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
EPS_DiagRq = can.Message(arbitration_id= 0x69A,                          
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================EPS_2===============================
EPS_2_DiagRq_HW = can.Message(arbitration_id= 0x6AB,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
EPS_2_DiagRq_HW_Rv = can.Message(arbitration_id=0x6AB,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
EPS_2_DiagRq_SW = can.Message(arbitration_id= 0x6AB,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
EPS_2_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6AB,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
EPS_2_DiagRq_Bootloader = can.Message(arbitration_id= 0x6AB,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
EPS_2_DiagRq = can.Message(arbitration_id= 0x69A,                           
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================ETG===============================
ETG_DiagRq_HW = can.Message(arbitration_id= 0x68E,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
ETG_DiagRq_HW_Rv = can.Message(arbitration_id=0x68E,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
ETG_DiagRq_SW = can.Message(arbitration_id= 0x68E,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
ETG_DiagRq_SW_Rv = can.Message(arbitration_id= 0x68E,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
ETG_DiagRq_Bootloader = can.Message(arbitration_id= 0x68E,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
ETG_DiagRq = can.Message(arbitration_id= 0x68E,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================FCAM===============================
FCAM_DiagRq_HW = can.Message(arbitration_id= 0x696,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
FCAM_DiagRq_HW_Rv = can.Message(arbitration_id=0x696,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
FCAM_DiagRq_SW = can.Message(arbitration_id= 0x696,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
FCAM_DiagRq_SW_Rv = can.Message(arbitration_id= 0x696,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
FCAM_DiagRq_CAL = can.Message(arbitration_id= 0x696,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
FCAM_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x696,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
FCAM_DiagRq_Bootloader = can.Message(arbitration_id= 0x696,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
FCAM_DiagRq = can.Message(arbitration_id= 0x696,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================SCAM===============================
SCAM_DiagRq_HW = can.Message(arbitration_id= 0x6A6,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
SCAM_DiagRq_HW_Rv = can.Message(arbitration_id=0x6A6,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
SCAM_DiagRq_SW = can.Message(arbitration_id= 0x6A6,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
SCAM_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6A6,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
SCAM_DiagRq_CAL = can.Message(arbitration_id= 0x6A6,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
SCAM_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6A6,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
SCAM_DiagRq_Bootloader = can.Message(arbitration_id= 0x6A6,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
SCAM_DiagRq = can.Message(arbitration_id= 0x6A6,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================GS===============================
GS_DiagRq_HW = can.Message(arbitration_id= 0x690,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
GS_DiagRq_HW_Rv = can.Message(arbitration_id=0x690,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
GS_DiagRq_SW = can.Message(arbitration_id= 0x690,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
GS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x690,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
GS_DiagRq_Bootloader = can.Message(arbitration_id= 0x690,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
GS_DiagRq = can.Message(arbitration_id= 0x690,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================HUD===============================
HUD_DiagRq_HW = can.Message(arbitration_id= 0x68D,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
HUD_DiagRq_HW_Rv = can.Message(arbitration_id=0x68D,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
HUD_DiagRq_SW_APP = can.Message(arbitration_id= 0x68D,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 4, 255, 255, 255, 255],
                  check = False)
HUD_DiagRq_SW_APP_Rv = can.Message(arbitration_id= 0x68D,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 68, 255, 255, 255, 255],
                  check = False)
HUD_DiagRq_SW_BASIC = can.Message(arbitration_id= 0x68D,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 5, 255, 255, 255, 255],
                 check = False)
HUD_DiagRq_SW_BASIC_Rv = can.Message(arbitration_id= 0x68D,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 69, 255, 255, 255, 255],
                  check = False)
HUD_DiagRq_HMI = can.Message(arbitration_id= 0x68D,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 6, 255, 255, 255, 255],
                 check = False)
HUD_DiagRq_HMI_Rv = can.Message(arbitration_id= 0x68D,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 70, 255, 255, 255, 255],
                  check = False)
HUD_DiagRq_Bootloader = can.Message(arbitration_id= 0x68D,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
HUD_DiagRq = can.Message(arbitration_id= 0x68D,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================IDB===============================
IDB_DiagRq_HW = can.Message(arbitration_id= 0x6A9,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
IDB_DiagRq_HW_Rv = can.Message(arbitration_id=0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
IDB_DiagRq_SW = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
IDB_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
IDB_DiagRq_CAL = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
IDB_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
IDB_DiagRq_Bootloader = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
IDB_DiagRq = can.Message(arbitration_id= 0x6A9,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================MHU===============================
MHU_DiagRq_PU = can.Message(arbitration_id= 0x684,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
MHU_DiagRq_PU_Rv = can.Message(arbitration_id=0x684,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
MHU_DiagRq_HW = can.Message(arbitration_id= 0x684,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
MHU_DiagRq_HW_Rv = can.Message(arbitration_id=0x684,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
MHU_DiagRq_SW = can.Message(arbitration_id= 0x684,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
MHU_DiagRq_SW_Rv = can.Message(arbitration_id= 0x684,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
MHU_DiagRq_TBOX = can.Message(arbitration_id= 0x684,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 100, 255, 255, 255, 255],
                 check = False)
MHU_DiagRq_TBOX_Rv = can.Message(arbitration_id= 0x684,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 73, 255, 255, 255, 255],
                  check = False)
MHU_DiagRq_Bootloader = can.Message(arbitration_id= 0x684,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
MHU_DiagRq = can.Message(arbitration_id= 0x684,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================MRGEN===============================
MRGEN_DiagRq_HW = can.Message(arbitration_id= 0x6A5,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
MRGEN_DiagRq_HW_Rv = can.Message(arbitration_id=0x6A5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
MRGEN_DiagRq_SW = can.Message(arbitration_id= 0x6A5,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
MRGEN_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6A5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
MRGEN_DiagRq_Bootloader = can.Message(arbitration_id= 0x6A5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
MRGEN_DiagRq = can.Message(arbitration_id= 0x6A5,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================OCS_P===============================
OCS_P_DiagRq_HW = can.Message(arbitration_id= 0x6C4,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
OCS_P_DiagRq_HW_Rv = can.Message(arbitration_id=0x6C4,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
OCS_P_DiagRq_SW = can.Message(arbitration_id= 0x6C4,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
OCS_P_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6C4,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
OCS_P_DiagRq_Bootloader = can.Message(arbitration_id= 0x6C4,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
OCS_P_DiagRq = can.Message(arbitration_id= 0x6C4,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================PAS===============================
PAS_DiagRq_HW = can.Message(arbitration_id= 0x697,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
PAS_DiagRq_HW_Rv = can.Message(arbitration_id=0x697,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
PAS_DiagRq_SW = can.Message(arbitration_id= 0x697,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
PAS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x697,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
PAS_DiagRq_Bootloader = can.Message(arbitration_id= 0x697,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
PAS_DiagRq = can.Message(arbitration_id= 0x697,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================POD_DCDC===============================
POD_DCDC_DiagRq_HW = can.Message(arbitration_id= 0x6BD,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
POD_DCDC_DiagRq_HW_Rv = can.Message(arbitration_id=0x6BD,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
POD_DCDC_DiagRq_SW = can.Message(arbitration_id= 0x6BD,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
POD_DCDC_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6BD,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
POD_DCDC_DiagRq_CAL = can.Message(arbitration_id= 0x6BD,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
POD_DCDC_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6BD,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
POD_DCDC_DiagRq_Bootloader = can.Message(arbitration_id= 0x6BD,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
POD_DCDC_DiagRq = can.Message(arbitration_id= 0x6BD,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================POD_GW===============================
POD_GW_DiagRq_HW = can.Message(arbitration_id= 0x6BF,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
POD_GW_DiagRq_HW_Rv = can.Message(arbitration_id=0x6BF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
POD_GW_DiagRq_SW = can.Message(arbitration_id= 0x6BF,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
POD_GW_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6BF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
POD_GW_DiagRq_CAL = can.Message(arbitration_id= 0x6BF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
POD_GW_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6BF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
POD_GW_DiagRq_Bootloader = can.Message(arbitration_id= 0x6BF,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
POD_GW_DiagRq = can.Message(arbitration_id= 0x6BF,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================POD_OBC===============================
POD_OBC_DiagRq_HW = can.Message(arbitration_id= 0x6BE,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
POD_OBC_DiagRq_HW_Rv = can.Message(arbitration_id=0x6BE,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
POD_OBC_DiagRq_SW = can.Message(arbitration_id= 0x6BE,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
POD_OBC_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6BE,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
POD_OBC_DiagRq_CAL = can.Message(arbitration_id= 0x6BE,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
POD_OBC_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6BE,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
POD_OBC_DiagRq_Bootloader = can.Message(arbitration_id= 0x6BE,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
POD_OBC_DiagRq = can.Message(arbitration_id= 0x6BE,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================RCU===============================
RCU_DiagRq_HW = can.Message(arbitration_id= 0x6A7,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
RCU_DiagRq_HW_Rv = can.Message(arbitration_id=0x6A7,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
RCU_DiagRq_SW = can.Message(arbitration_id= 0x6A7,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
RCU_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6A7,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
RCU_DiagRq_CAL = can.Message(arbitration_id= 0x6A7,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
RCU_DiagRq_CAL_Rev = can.Message(arbitration_id= 0x6A7,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
RCU_DiagRq_Bootloader = can.Message(arbitration_id= 0x6A7,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
RCU_DiagRq = can.Message(arbitration_id= 0x6A7,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================SHVU_F===============================
SHVU_F_DiagRq_HW = can.Message(arbitration_id= 0x6C2,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
SHVU_F_DiagRq_HW_Rv = can.Message(arbitration_id=0x6C2,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
SHVU_F_DiagRq_SW = can.Message(arbitration_id= 0x6C2,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
SHVU_F_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6C2,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
SHVU_F_DiagRq_Bootloader = can.Message(arbitration_id= 0x6C2,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
SHVU_F_DiagRq = can.Message(arbitration_id= 0x6C2,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================SHVU_R===============================
SHVU_R_DiagRq_HW = can.Message(arbitration_id= 0x6C3,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
SHVU_R_DiagRq_HW_Rv = can.Message(arbitration_id=0x6C3,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
SHVU_R_DiagRq_SW = can.Message(arbitration_id= 0x6C3,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
SHVU_R_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6C3,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
SHVU_R_DiagRq_Bootloader = can.Message(arbitration_id= 0x6C3,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
SHVU_R_DiagRq = can.Message(arbitration_id= 0x6C3,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================SRR_FL===============================
SRR_FL_DiagRq_HW = can.Message(arbitration_id= 0x6B5,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
SRR_FL_DiagRq_HW_Rv = can.Message(arbitration_id=0x6B5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
SRR_FL_DiagRq_SW = can.Message(arbitration_id= 0x6B5,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
SRR_FL_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6B5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
SRR_FL_DiagRq_Bootloader = can.Message(arbitration_id= 0x6B5,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
SRR_FL_DiagRq = can.Message(arbitration_id= 0x6B5,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================SRR_FR===============================
SRR_FR_DiagRq_HW = can.Message(arbitration_id= 0x6B4,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
SRR_FR_DiagRq_HW_Rv = can.Message(arbitration_id=0x6B4,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
SRR_FR_DiagRq_SW = can.Message(arbitration_id= 0x6B4,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
SRR_FR_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6B4,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
SRR_FR_DiagRq_Bootloader = can.Message(arbitration_id= 0x6B4,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
SRR_FR_DiagRq = can.Message(arbitration_id= 0x6B4,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================SRR_RL===============================
SRR_RL_DiagRq_HW = can.Message(arbitration_id= 0x6B7,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
SRR_RL_DiagRq_HW_Rv = can.Message(arbitration_id=0x6B7,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
SRR_RL_DiagRq_SW = can.Message(arbitration_id= 0x6B7,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
SRR_RL_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6B7,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
SRR_RL_DiagRq_Bootloader = can.Message(arbitration_id= 0x6B,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
SRR_RL_DiagRq = can.Message(arbitration_id= 0x6B7,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================SRR_RR===============================
SRR_RR_DiagRq_HW = can.Message(arbitration_id= 0x6B6,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
SRR_RR_DiagRq_HW_Rv = can.Message(arbitration_id=0x6B6,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
SRR_RR_DiagRq_SW = can.Message(arbitration_id= 0x6B6,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
SRR_RR_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6B6,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
SRR_RR_DiagRq_Bootloader = can.Message(arbitration_id= 0x6B6,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
SRR_RR_DiagRq = can.Message(arbitration_id= 0x6B6,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================VCU===============================
VCU_DiagRq_HW = can.Message(arbitration_id= 0x6AC,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_HW_Rv = can.Message(arbitration_id=0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_HW = can.Message(arbitration_id= 0x6AC,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_HW_Rv = can.Message(arbitration_id=0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_SW = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
VCU_DiagRq_SW_Rv = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_SW_APP = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 4, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_SW_APP_Rv = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 68, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_SW_BASIC = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 5, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_SW_BASIC_Rv = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 69, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_CAL = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_CAL_Rv = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq_Bootloader = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
VCU_DiagRq = can.Message(arbitration_id= 0x6AC,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================XGW===============================
XGW_DiagRq_PU = can.Message(arbitration_id= 0x682,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 3, 255, 255, 255, 255],
                  check = False)
XGW_DiagRq_PU_Rv = can.Message(arbitration_id=0x682,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 67, 255, 255, 255, 255],
                  check = False)
XGW_DiagRq_HW = can.Message(arbitration_id= 0x682,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
XGW_DiagRq_HW_Rv = can.Message(arbitration_id=0x682,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
XGW_DiagRq_SW = can.Message(arbitration_id= 0x682,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
XGW_DiagRq_SW_Rv = can.Message(arbitration_id= 0x682,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
XGW_DiagRq_CAL = can.Message(arbitration_id= 0x682,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 2, 255, 255, 255, 255],
                  check = False)
XGW_DiagRq_CAL_Rv = can.Message(arbitration_id= 0x682,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 66, 255, 255, 255, 255],
                  check = False)
XGW_DiagRq_Bootloader = can.Message(arbitration_id= 0x682,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
XGW_DiagRq = can.Message(arbitration_id= 0x682,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================YSS===============================
YSS_DiagRq_HW = can.Message(arbitration_id= 0x68F,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
YSS_DiagRq_HW_Rv = can.Message(arbitration_id=0x68F,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
YSS_DiagRq_SW = can.Message(arbitration_id= 0x68F,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
YSS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x68F,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
YSS_DiagRq_Bootloader = can.Message(arbitration_id= 0x68F,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
YSS_DiagRq = can.Message(arbitration_id= 0x68F,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#=========================SS===============================
SS_DiagRq_HW = can.Message(arbitration_id= 0x690,
                is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 145, 255, 255, 255, 255],
                  check = False)
SS_DiagRq_HW_Rv = can.Message(arbitration_id=0x690,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 65, 255, 255, 255, 255],
                  check = False)
SS_DiagRq_SW = can.Message(arbitration_id= 0x690,
                  is_extended_id= 0,
                 dlc= 8,data=[3, 34, 241, 136, 255, 255, 255, 255],
                 check = False)
SS_DiagRq_SW_Rv = can.Message(arbitration_id= 0x690,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 72, 255, 255, 255, 255],
                  check = False)
SS_DiagRq_Bootloader = can.Message(arbitration_id= 0x690,
                  is_extended_id= 0,
                  dlc= 8,data=[3, 34, 241, 1, 255, 255, 255, 255],
                  check = False)
SS_DiagRq = can.Message(arbitration_id= 0x690,
                  is_extended_id= 0,
                  dlc= 8,data=[48, 0, 20, 255, 255, 255, 255, 255],
                  check = False)
#===========================Creat window================================
def Hardware_Config():
      subprocess.call('C://Windows//System32//vcanconf.exe')

