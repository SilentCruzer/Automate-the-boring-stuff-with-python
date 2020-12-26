from pathlib import Path
import re

location = Path.cwd()
regex = input("Enter regex: ")
searchfor = re.compile(regex)

for file in list(location.glob('*.txt')):
	with open(file) as f:
		lines = f.readlines()
		for word in lines:
			if searchfor.search(regex)	:
				print('Found the following line:\n'+ word )
