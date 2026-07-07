from datetime import datetime 
import psutil 

cpu = psutil.porcent_cpu(interval=1)
print (cpu)
now = datetime.now()
print (now)
