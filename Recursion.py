


import os 
import datetime

#DirList = [...]


def recurs(Directory):
	
	# Directory would be os.path at first 
	# ex. D:/workspace/python/
	DirectoryList = Directory.split("/")
	# Result: ['D:','workspace', 'python']
	
	
	OsDir = os.listdir(Directory)
	# Example Output: 
	# [test.htm, stamp, faq.htm, _vti_txt, robots.txt, itemlisting, resumelisting, writing_effective_resume.htm, advertisebusiness.htm, papers, resume]
	
	
	for val in OsDir:
	
		tempDir = DirectoryList.append(val)
		
		if Directory.isfile(tempDir):#If the value is a file
			#Where we would be hashing and printing the time and stuff
			print(val)
			
			#From the datetime library to print the date and time
			now = datetime.datetime.now()
			print ("Current date and time for %S: ", val)
			print (now.strftime("%Y-%m-%d %H:%M:%S"))

			
		elif Directory.isDir(tempDir):#If the value is a directory

			recurs(tempDir)
