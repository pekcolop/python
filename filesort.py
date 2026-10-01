import os, shutil
'''importing these will allow us to organise edit
and manipulate files and directories accross operating systems'''

path = r"C:/Users/InternalLedger/Desktop/test folder/"
#this is the location of where we want our files to be organised
#r is used so that backslashes are not read when searching for the path

file_name = os.listdir(path)
#this shows us what is actually stored in the path
#also needs to be named to call it later on in the code

folder_names = ['csv files', 'image files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))
#this section checks to see if there are folders already
#if not then they are created

#this section now begins to sort the files into their respective folders
#this is repeated for each file type, and checks to see if the file already exists in the folder before moving it
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
            shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
                shutil.move(path + file, path + "text files/" + file)
    else:
          print("File already exists in the folder or is not a supported file type")            

#if a file already exists in the folder, it will not be moved and a message will be printed to the console

