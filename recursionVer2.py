# Name: Christopher Meacham
# Subject: SY402 Lab 08 Version 2
# Description: This is a python file that utilizes recursion in order to sort through multiple file directories. The libraries used are the os, datetime, and sys libraries. The file takes in input from the user's command line for the desired directory. The file then utilizes the os library by making a list of the 1st level directories and files in a given location (os.listdir()) and then checking later on whether or not the values in the directory list (from os.listdir()) is a file or a directory. If the value is a file, then it will print out the file name, its directory, and the time at which this was done (utilizing the datetime library). If the value is a directory, the function will call itself, but this time, will use the original directory with the appended directory value at the end of it. Essentially going through the same process, but within one more level into a directory. There are certain directories that should not be looked into, those are listed after the value is detected to be a directory.

import os 
import datetime
import sys


def recurs(Directory):
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
            # Where we would be hashing and printing the time and stuff
            print(tempDir)

            # From the datetime library to print the date and time
            now = datetime.datetime.now()
            print("Current date and time for : "+ val)
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print()        

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
                recurs(tempDir)# Recursively go further into the directories to print the file names
                
        DirectoryList.pop() # Done with that file/directory and will need to continue going through the list


def main():
    
    recurs(sys.argv[1])


main()