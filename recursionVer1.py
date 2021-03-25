import os
import datetimeimport hashlib

DirList = []

def recurs(Directory):

	#Directory would be os.path at first
	# ex. D:/workspace/python/

	DirectoryList = Directory.split("/")
	#Result: {'D:'workspace', 'python'}

	OsDir = os.listdir(Directory)
	'''
	'''
	for val in OsDir:
		print(val)
		tempDir = DirectoryList.append(val)
		
		if os.path.isfile(tempdir)
			print(val)
			now = datetime.datetime.now()
			print("Current date and time for %S: ", val)
			print(now.strftime("%Y-%m-%d %H:%M:%S"))
		#	hash = hashlib.sha256()
		#	hash.update(val)
		#	print(hash.hexdigest())
		
			
			
		elif Directory.isDir(tempdir):
			recurs(tempdir)
			
recurs("/test")
