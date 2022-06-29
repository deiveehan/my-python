import time
import datetime
import sounddevice as sd


while(True):
    now = datetime.datetime.now()
    print(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    
    if(now.hour == 10 and now.minute == 42): 
        print("STOCK MARKET STARTS ---> All the best")
    time.sleep(30)