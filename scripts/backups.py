import shutil
import os
from datetime import datetime

def backup_file(source, destination):
    os.makedirs (destination,exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_name = f"{destination}/pipe_{timestamp}.txt"
   
    shutil.copytree(source, backup_name)

    print("Backup completed!")

backup_file("/home/brayan/cloudenginner/README.md/" , "/home/brayan/cloudenginner/README.md/scripst/backups/")