import psutil
from datetime import datetime

cpu = psutil.cpu_percent(interval=1)
ram =psutil.virtual_memory().percent
disk =psutil.disk_usage("/").percent
time = datetime.now().strftime("%Y-%m-%D%H:%M:%S")
server = (cpu,
          ram,
          disk)


print(f"""the server is online today {time}
the result:
cpu:{cpu}
ram:{ram}
disk:{disk}""")


