import os,shutil

def gaps(path, prefix):
	file_num  = 0 

	for foldername,subfolder, filename in os.walk(path):
		for name in filename:
			if name.startswith(prefix):
				name.split(prefix)
				number, extension = name.split('.')
				print(number)


gaps('/home/silentcruzer/Automate-the-boring-stuff-with-python/Chapter-10','spam001')
