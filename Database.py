import cantools
from pprint import pprint
db = cantools.database.load_file('C:/Users/VGADMIN/Desktop/Python/16_Diag_CAN_Matrix_V11.3.dbc')
for i in range(100):
    try:
        print(db.messages[i].name,db.messages[i].senders,db.messages[i].length,hex(db.messages[i].frame_id),db.messages[i].cycle_time,'\n')
    except IndexError:
        break