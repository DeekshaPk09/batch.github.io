import time
import sys
while(True):
   curr_time = time.localtime()
   curr_clock = time.strftime("%H:%M:%S", curr_time)
   print(curr_clock)
   hour=curr_clock[:2]
   min=curr_clock[3:5]
   hour=int(hour)
   min=int(min)
   hours=hour*4
   mins=min/15
   res=int(hours+mins)
   if(min%15!=0):
      res=int(hours+mins)+1
   print('Batch number is:',res)
   sys.stdout.flush()
   print("\r"),
   time.sleep(1)

