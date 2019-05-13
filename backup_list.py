import os
import time


def desktop():
    try:
        command = 'python backup_desktop.py'
        os.system(command)
    except:
        desktop()




def software():
    try:
        command = 'python backup_software.py'
        os.system(command)
    except:
        software()





def Project():
    try:
        command = 'python backup_project.py'
        os.system(command)
    except:
        Project()



