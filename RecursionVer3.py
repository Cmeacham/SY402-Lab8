# Name: Christopher Meacham
# Subject: SY402 Lab 08 Version 3
# Description: This version of the recursive file has the same functionalities as the previous version. The only difference is that this implements the use of the SHA256 hashing algorithm found in the hashlib library. No notable differences other that that as well as the python script opening a log file to store the SHA256 hashes along with the files' info.

import os 
import datetime
import sys
import hashlib


def recurs(Directory, Log, sha):
    # Directory would be os.path at first 
    # ex. D:/workspace/python/
    DirectoryList = Directory.split("/")
    # Result: ['D:','workspace', 'python']

    OsDir = os.listdir(Directory)
    # Example Output: 
    # [test.htm, stamp, faq.htm, _vti_txt, robots.txt, itemlisting, resumelisting, writing_effective_resume.htm, advertisebusiness.htm, papers, resume]
    
    for val in OsDir:
        
        DirectoryList.append(val)
        tempDir = "/".join(DirectoryList)# Will bring the list back to a directory format such as '/home/meach/Documents/SY485'
                
        if os.path.isfile(tempDir):# If the value is a file
            
            # Creating the sha256 hash of the file
            tempRead = open(tempDir, "rb")
            for block in iter(lambda: tempRead.read(4096),b""):
                sha.update(block)   
            
            
            # Where we would be hashing and printing the time and stuff
            print(tempDir)
            
            # From the datetime library to print the date and time
            now = datetime.datetime.now()
            print("Current date and time for : "+ val)
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print() 
            
            #Store everything into the log file 
            # *file directory*
            # *file's hash*
            # *time/date of observation*
            Log.write(tempDir+"\n"+sha.hexdigest()+"\n"+now.strftime("%Y-%m-%d %H:%M:%S")+"\n\n")    

        if os.path.isdir(tempDir): #If the value is a directory
            if ("dev"== val) or ("proc" == val) or ("run" == val) or ("sys" == val) or ("tmp" == val) or ("lib" == val) or ("run" == val):
                # These are the directories we don't want to go into
                '''
                /dev
                /proc
                /run
                /sys
                /tmp
                /var/lib
                /var/run
                '''    
                        
            else:
                recurs(tempDir, Log, sha)# Recursively go further into the directories to print the file names
                
        DirectoryList.pop() # Done with that file/directory and will need to continue going through the list


def main():
    
    shaVal = hashlib.sha256()
    Ofile = open("RecursiveLog.txt", "w")
    recurs(sys.argv[1], Ofile, shaVal)
    
    Ofile.close()


main()