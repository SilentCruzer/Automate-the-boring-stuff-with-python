import os,shutil

def gaps(path, prefix):
	file_num  = 0 

	for foldername,subfolder, filename in os.walk(path):
		for name in filename:
			if name.startswith(prefix):
				name.split(prefix)
				number, extension = name.split('.')
				print(number)

path = ''
gaps(path,'spam001')
