import os,shutil

def copy(copy_from , copy_to):
	for foldername,subfolder, filename in os.walk(copy_from):
		print(foldername)
		for name in filename:
			if name.endswith(".txt"):
				print(name)
				shutil.copy(os.path.join(str(foldername), name), copy_to)

#Enter the path of the folder you want to copy from
From = ''
#Enter the path of the folder to paste the file.
To = ''

copy(From,To) 