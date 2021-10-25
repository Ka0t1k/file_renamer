from os.path import exists
import os

#expects a file named rename.csv in the same directory. 
#the format of the file is the directory of the file (i.e. "C:\Users\user\file_rename_csv\rename"), 
#                          the current name of the file
#                          the new file name


file_exists = exists("rename.csv")
#os.remove("rename.csv")

if(file_exists):
    with open("rename.csv") as file:
        #iterate through the lines in rename.csv
        for line in file:
            #expects the csv to be comma delmited
            files = line.split(",")
            #change the current directory to the directory specified in the csv
            os.chdir(files[0])
                
            #if the file exists in the directory then rename it
            if exists(files[1]):
                os.rename(files[1], files[2].rstrip())
            else:
                print(files[1] + " not found")
