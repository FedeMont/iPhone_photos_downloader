import os, shutil, time
from datetime import datetime

#iPhone media on linux pcs are in -> /run/user/1000/gvfs/gphoto2:host=*/
os.chdir("/run/user/1000/gvfs/") #change directory to "/run/user/1000/gvfs/"

for i in os.listdir(): #find the 'gphoto2:host=*' directory
        if "gphoto2:host=" in i:
            os.chdir(i) #change directory to "../gphoto2:host=*"
            break

if os.getcwd() != '/run/user/1000/gvfs':
    pictures= "~/Pictures" #computer directory where it will save the photos
    os.chdir("DCIM/") #change directory to /run/user/1000/gvfs/gphoto2:host=*/DCIM/
    num_of_photos=1
    for i in os.listdir(os.getcwd()): #directory list of DCIM directory
        os.chdir(i) #change directory for every directory in DCIM
        for j in os.listdir(os.getcwd()): #media list in the current directory=> i
            currentIDirectory = os.getcwd()
            print(j)
            creationDate= str(datetime.fromtimestamp(os.stat(j).st_ctime))[:7] #media creation date in 'year-month' format
                                                                                #on linux it is the last modification date
            os.chdir(pictures) #change directory to "~/Pictures/"
            directoryExist= False
            for x in os.listdir(os.getcwd()): #directory list of Pictures directory
                if creationDate==x:
                    directoryExist= True
                    break yet
                '''else:
                    directoryExist= False'''
            if directoryExist: #the directory named 'creationDate' already exists
                #copy-paste j in creationDate directory
                os.chdir(creationDate)
                photoExist= False
                for y in os.listdir(os.getcwd()): #media list in the current directory=> creationDate
                    if j==y:
                        photoExist= True
                        break
                    '''else:
                        photoExist= False'''
                if not photoExist: #media hasn't been downloaded yet
                    shutil.copy2((currentIDirectory+"/"+j), (pictures+"/"+creationDate))
                    print(num_of_photos +" directory exist=> "+(currentIDirectory+"/"+j)+" copied to => "+(pictures+"/"+creationDate))
            else: #the directory named 'creationDate' doesn't exists
                os.mkdir(creationDate) #create the directory named creationDate
                #copy-paste j in creationDate directory
                os.chdir(creationDate)
                shutil.copy2((currentIDirectory+"/"+j), (pictures+"/"+creationDate))
                print(num_of_photos +" directory doesn't exist=> "+(currentIDirectory+"/"+j)+" copied to => "+(pictures+"/"+creationDate))
            num_of_photos+=1
            os.chdir(currentIDirectory) #return to the directory 'i'
        os.chdir("..") #change directory to the upper directory
else: #iPhone is not connected
    print("There's no iPhone")
