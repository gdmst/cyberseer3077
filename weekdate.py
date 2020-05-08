import datetime 
import calendar 
date = '2000-05-04'
Dayone=['วันจันทร์','วันอังคาร','วันพุธ','วันพฤหัส','วันศุกร์','วันเสาร์','วันอาทิตย์']
mounthone=['','มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
def findDay(date): 
    born=datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return Dayone[born]
def cutm(date):
   mounth=date.split('-')[1]
   return mounth
def cutd(date):
    day=date.split('-')[2]
    return day
def checkd(dateNo):
    if dateNo[0] == '0' : dateNo=dateNo[1]
    return dateNo

def checkm(mounthNo):
    if mounthNo[0] == '0' : mounthNo=mounthNo[1]
    return mounthNo

def getm(xNo):
    num=xNo
    return mounthone[num]

print(findDay(date))
dateNo=cutd(date)
print(checkd(dateNo))
mounthNo=cutm(date)
x=checkm(mounthNo)
xNo=int(x)
print(getm(xNo))




    

   
