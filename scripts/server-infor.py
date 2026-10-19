import psutil


cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

def monitor_01(cpu, ram, disk):
    
    if cpu <= 65:
         result1 = ("it's cool")
    elif cpu >= 89:
         result1 = ("it's so hot")
    else:
         result1 = ("it's normal")

    if ram <= 65:
            result2 = ("it's cool")
    elif ram >= 89:
            result2 = ("it's so hot")
    else:
             result2 = ("it's normal")
           
    if disk <= 65:
        result3 = ("it's cool")
    elif disk >= 89:
         result3 = ("it's so hot")
    else:
         result3 = ("it's normal")






print (monitor_01)