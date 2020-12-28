import os,shutil

def delete(path):
	for foldername,subfolder, filename in os.walk(path):
		for name in filename:
			filepath = os.path.join(path, name)
			size = os.path.getsize(filepath)
			if size > 1000000:
				print(filepath)
		

path = ''
delete(path)