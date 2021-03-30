# Name: Christopher Meacham and Mary-Margaret West
# Subject: SY402 Lab 08 Version 4
# Description: This version of the recursive file has the same functionalities as the previous version. The only update to this one is that it checks the already made log file and updates the hashes of the files then prints out a summary of any new files, missing files, or modified.

import os 
import datetime
import sys
import hashlib

# These will keep track of any modified or new files found in the directories
# Made them global variables to allow for both main() and recurs() to use
NewF = []
ModF = []
MissF = []
ComprtoMiss = []

# Recursive Function ---------------------------------------------------------------------------------------------------
def recurs(Directory, LogList, WriteLog): #sha): 
    
    #The directories we should not be worrying about
    NoGoList = ["/dev","/proc","/run","/sys","/tmp","/var/lib", "/var/run"]
    
    rootDir = "No"
    # Directory would be os.path at first 
    # ex. D:/workspace/python/
    DirectoryList = Directory.split("/")
    # Result: ['D:','workspace', 'python']
    
    if Directory == "/":
        rootDir = "Yes"
    

    OsDir = os.listdir(Directory)
    # Example Output: 
    # [test.htm, stamp, faq.htm, _vti_txt, robots.txt, itemlisting, resumelisting, writing_effective_resume.htm, advertisebusiness.htm, papers, resume]
    
    
    # Sorting of the files in the directory list discovered earlier -----------------------------------
    for val in OsDir:
        
        # Will bring the list back to a directory format --------------------
        DirectoryList.append(val)
        tempDir = "/".join(DirectoryList)
        if rootDir == "Yes":
            tempDir = tempDir[1:]
        # '/home/meach/Documents/SY485' <-- Example of how it will look
        # -------------------------------------------------------------------
            
        # This checks if the path given is a file using .isfile() function from os library
        if os.path.isfile(tempDir):
            # Adding to the Compare list to use for later with MissF
            ComprtoMiss.append(tempDir)
            
            # Creating the sha256 hash of the file ----------------
            tempRead = open(tempDir, "rb").read()
            sha = hashlib.sha256(tempRead).hexdigest()
            # -----------------------------------------------------
            
            # This portion checks if the file is new or modified ------
            if (tempDir in LogList) and (sha != LogList[LogList.index(tempDir)+1]):
                ModF.append(tempDir) 
            
            elif tempDir not in LogList:
                NewF.append(tempDir)
            # ----------------------------------------------------------------------
            
            # Either it's an update or addition, they both are still written to the log file
            print(tempDir)
            
            # From the datetime library to print the date and time ----------
            now = datetime.datetime.now()
            print("Current date and time for : "+ val)
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print() 
            # ---------------------------------------------------------------
            
            
            # Store everything into the log file 
            # *file directory*
            # *file's hash*
            # *time/date of observation*
            WriteLog.write(tempDir+"\n"+sha+"\n"+now.strftime("%Y-%m-%d %H:%M:%S")+"\n\n")    

        # This checks if the path given is a directory using .isdir() function from os library
        if os.path.isdir(tempDir):
            
            # Checks to make sure the directory isn't in the list of directories to not go into 
            if val not in NoGoList:
                # Recursively go further into the directories to print the file names
                recurs(tempDir, LogList, WriteLog) # sha)
        
        
        # Done with that file/directory and will need to continue going through the list
        DirectoryList.pop() 
    
    # End of for loop --> done going through the directory given ---------------------------------------

# Main Function --------------------------------------------------------------------------------------------------------
def main():

        
    # Will be used later on for the hashing portion
    # shaVal = hashlib.sha256()
    
    # If the file we need to read exists or not using .exists() from os library----------------------
    if os.path.exists(os.getcwd()+"/RecursiveLog.txt"):
        ReadFile = open("RecursiveLog.txt", "r").read().split("\n")
    else:
        TempOpenFile = open("RecursiveLog.txt", "w").close()
        ReadFile = open("RecursiveLog.txt", "r").read().split("\n")
    # -----------------------------------------------------------------------------------------------
    
    # Where we will be logging the information    
    WriteFile = open("RecursiveLog.txt", "w")

    # **All inputs for the recursion function are set**
    # Recursion starts here ------------------------------------
    recurs(sys.argv[1], ReadFile, WriteFile) #shaVal
    
    WriteFile.close()
    # ----------------------------------------------------------
    
    # Check to see which files have been modified, added, or are missing from the previous log -------------
    # This is where we figure out what files are missing
    for item in ReadFile:
        if (item not in ComprtoMiss) and ("/" in item):
            MissF.append(item)
    
    print("#################### Summary #########################\n")
    print("Modified Files:")
    if len(ModF) == 0:
        print("None\n") 
    else:
        print("\n".join(ModF)+"\n")
    
    print("New Files:")
    if len(NewF) == 0:
        print("None\n")
    else:
        print("\n".join(NewF)+"\n")

    print("Missing Files:")
    if len(MissF) == 0:
        print("None")
    else:
        print("\n".join(MissF))    
    
    # ------------------------------------------------------------------------------------------------------

main()
