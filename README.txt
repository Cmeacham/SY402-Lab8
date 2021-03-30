# Name: Christopher Meacham and Mary-Margaret West

# Subject : SY402 LAB 8 Python File 

# Title: hash.py 

# File Description : 


This is a python file that utilizes recursion in order to sort through multiple file directories. The libraries used are the os, datetime, sys and hashlib libraries. The file takes in input from the user's command line for the desired directory. The file then utilizes the os library by making a list of the 1st level directories and files in a given location (os.listdir()) and then checking later on whether or not the values in the directory list (from os.listdir()) is a file or a directory. If the value is a file, then it will print out the file name, its directory, and the time at which this was done (utilizing the datetime library). In addition, by the use of the SHA256 hashing algorithm found in the hashlib library, the python script will open a log file to store the SHA256 hashes of the file contents, along with the files' other information (previously discussed). If the value is a directory, the function will call itself, but this time, will use the original directory with the appended directory value at the end of it. Essentially going through the same process, but within one more level into a directory. There are certain directories that should not be looked into, those are listed after the value is detected to be a directory. From the log file created, this program will also check and update the hashes of the files then prints out a summary of any new files, missing files, or modified.

