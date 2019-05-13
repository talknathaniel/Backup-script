import os
import threading
os.system("cls")
from backup_list import *
import getpass
password = '70321016021'
print("Starting Backup\n\n")
check = 'yes'
if(check=='yes'):
    code = password#getpass.getpass("Authorisation ID:-")
    if(code== password):
        #print("\n\nAuthorisation successfull\n\n")
        disk = input("Please confirm you have inserted the disk:- ")
        if(disk=='yes'):
            print("Checking")
            path = 'D:\\Nathaniel\\Backup'
            ch =os.path.exists(path)
            if(ch==True):
                print("\n\nBackup\n\n")
                t1 = threading.Thread(target=desktop)
                t2=threading.Thread(target=Project)
                t1.start()
                t2.start()
                print("\n\nFinished\n\n")
                t1.join() 
                t2.join() 
                print("Done!") 
