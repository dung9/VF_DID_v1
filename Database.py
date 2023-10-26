import cantools
from pprint import pprint
db = cantools.database.load_file('C:/Users/DungHoang/Downloads/Python/03_Body_CAN_Matrix_BEV_V9.2.1.dbc')
index = 0
for i in range(1000):
    try:
        index +=1
        #print(db.messages[i].name,db.messages[i].senders,db.messages[i].length,hex(db.messages[i].frame_id),db.messages[i].cycle_time,'\n')
        print(db.messages[i].name)
    except IndexError:
        break
index_signal = 0
for i in range(20):
    try:
        index_signal +=1
        print(db.messages[8].signals[i].name)
    except IndexError:
        break
print(index)
print(index_signal)