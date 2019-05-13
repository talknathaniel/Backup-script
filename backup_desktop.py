import os
import shutil
from datetime import date
today = date.today()
os.system("cls")





back_folder = 'N:\computer\Desktop'
os.chdir(back_folder)


#back_folder_to = input("\nFolder path you want to backup to:- ")
today = str(today)
back_folder_to = "D:/Nathaniel/Backup/Desktop/Desktop " + today

shutil.copytree(back_folder,back_folder_to)

