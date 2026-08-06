print ("monitor is online")

import psutil
import datetime
import time 


cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory 
disk = psutil.disk_usage(interval=1)



def monitor_server(cpu,ram,disk):



    if cpu < 70: 
        print ("normal")

    elif cpu > 90: 
        print("super hot")

    else:
        print("hot")


    if ram < 70: 
            print ("normal")
    
    elif ram > 90: 
            print("super hot")
    
    else:
            print("hot")


    if disk < 70: 
            print ("normal")
    
    elif disk > 90: 
            print("super hot")
    
    else:
            print("hot")

   
 print (monitor_server(cpu,ram,disk))
    










