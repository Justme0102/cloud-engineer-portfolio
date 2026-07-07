print ("server")
import psutil
from datetime import datetime

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

def report_server(cpu, ram, disk):
       
        if cpu <= 75:
            status_cpu = "normal"

        elif cpu >= 90: 
            status_cpu = "dangerous"
        
        else:
            status_cpu = "hot"
      




        if ram <= 65:
            status_ram = "normal"
         
        elif ram >= 90: 
            status_ram = "dangerous"

        else:
            status_ram = "hot"
       



        if disk <= 65:
            status_disk = "normal"
         
        elif disk >= 90: 
            status_disk = "dangerous"

        else:
            status_disk = "hot"

        now = datetime.now()
       
        report = f""" 
===== SERVER REPORT ===== 
{now}
cpu:{status_cpu}
ram: {status_ram} 
disk: {status_disk}"""
      
        print (report)
        file = open("report.txt","a")
        file.write(report)
        file.write("\n\n")
        file.close()
report_server (cpu, ram, disk)













