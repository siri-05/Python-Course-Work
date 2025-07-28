'''productID=int(input("Enter Product ID: "))
productName=input("Enter Product Name: ")
price=float(input("Enter Price: "))
categories=input("Enter Categories(comma-separated): ").split(',')
stockDetails=(int(input("Enter Available Stock: ")),int(input("Enter Sold Stock: ")))
discount=float(input("Enter Discount Percentage: "))
productFeatures=set(input("Enter Product Features(comma-separated): ").split(','))
supplierDetails={"Name":input("Enter Supplier Name: "),"Contact":input("Enter Supplier Contact Number: "),"Location":input("Enter Supplier Location: ")}

print("Product ID, Name, Price: ",productID,", ",productName,", ",price)
print("Product Discount : %0.2f"%discount,"%")
print(f"Product Name: {productName}\nPrice: ₹{price}\nDiscount: {discount}%\nStock Available: {stockDetails[0]} units")
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(supplierDetails["Name"],supplierDetails["Contact"],supplierDetails["Location"]))'''

#Clock
from datetime import datetime, timezone, timedelta
app_version="15.10.3_f553dff_250608"
date_time=datetime.now()
kolkata_tz=datetime.now(timezone(timedelta(hours=5, minutes=30)))
london_tz=datetime.now(timezone(timedelta(hours=0, minutes=0)))
sydney_tz=datetime.now(timezone(timedelta(hours=9, minutes=0)))
newyork_tz=datetime.now(timezone(timedelta(hours=-5, minutes=0)))
world_clock={"Kolkata":kolkata_tz.strftime("%Y-%m-%d %H:%M:%S"), "London":london_tz.strftime("%Y-%m-%d %H:%M:%S"), "Sydney":sydney_tz.strftime("%Y-%m-%d %H:%M:%S"), "New York":newyork_tz.strftime("%Y-%m-%d %H:%M:%S")}
time_zone=input("Enter time zone(Kolkata/London/Sydney/New York): ")
time_format=int(input("Enter time format(12-hour/24-hour): "))
no_of_alarms=int(input("Enter how many alarms to set: "))
alarm=list()

#Datatypes of variables used
print("app_version: ",type(app_version))
print("date_time: ",type(date_time))
print("world_clock: ",type(world_clock))
print("time_zone: ",type(time_zone))
print("time_format: ",type(time_format))
print("no_of_alarms: ",type(no_of_alarms))
print("alarm: ",type(alarm))

#Set the alarms and print them
if time_format==12:
    for i in range(no_of_alarms):
        details=input("Enter alarm details(alarm_name, time, AM/PM, snooze, vibrate, repeat): ").split(", ")
        temp={"Alarm Name":details[0], "Time":details[1], "AM/PM":details[2], "Time Zone":world_clock[time_zone], "Snooze":details[3], "Vibrate":details[4], "Repeat":details[5]}
        alarm.append(temp)
else:
    for i in range(no_of_alarms):
        details=input("Enter alarm details(alarm_name, time, snooze, vibrate, repeat): ").split(", ")
        temp={"Alarm Name":details[0], "Time":details[1], "Time Zone":world_clock[time_zone], "Snooze":details[2], "Vibrate":details[3], "Repeat":details[4]}
        alarm.append(temp)
for i in range(no_of_alarms):
    if time_format==12:
        print("Alarms:\nAlarmName    Time           TimeZone       Snooze    Vibrate    Repeat")
        print(f"{alarm[i]['Alarm Name']}      {alarm[i]['Time']}{alarm[i]['AM/PM']}    {alarm[i]['Time Zone']}     {alarm[i]['Snooze']}        {alarm[i]['Vibrate']}        {alarm[i]['Repeat']}")
    else:
        print("Alarms:\nAlarmName    Time       TimeZone           Snooze    Vibrate      Repeat")
        print(f"{alarm[i]['Alarm Name']}        {alarm[i]['Time']}    {alarm[i]['Time Zone']}       {alarm[i]['Snooze']}        {alarm[i]['Vibrate']}       {alarm[i]['Repeat']}")