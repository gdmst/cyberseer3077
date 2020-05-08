import datetime 
import calendar 
date = '04-05-2000'
Dayone=['วันจันทร์','วันอังคาร','วันพุธ','วันพฤหัส','วันศุกร์','วันเสาร์','วันอาทิตย์']
def findDay(date): 
    born=datetime.datetime.strptime(date, '%d-%m-%Y').weekday()
    return Dayone[born]
print(findDay(date))
    

   

