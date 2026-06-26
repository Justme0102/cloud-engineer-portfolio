print ("status of server")

client1 = int(input("enter the cpu: "))
client2 = int(input("enter the ram: "))
client3 = int(input("enter the disk: "))

def report_server(cpu, ram, disk):
       
        if cpu <= 75:
                print("cpu-normal")

        elif cpu >= 80: 
                print ("cpu-hot") 
        
        elif cpu >= 90:
                print ("cpu-dangerous")

        if ram <= 65:
            print("ram-normal")
         
        elif ram >= 70: 
            print ("ram-hot")

        elif ram >= 90:
            print ("ram-dangerous")
        
        if disk <= 65:
            print("disk-normal")
         
        elif disk >= 70: 
            print ("disk-hot")

        elif disk >= 90:
            print ("disk-dangerous")
        

report_server (client1, client2,client3)


