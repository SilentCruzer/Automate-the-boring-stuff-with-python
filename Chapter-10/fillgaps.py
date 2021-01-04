import os,shutil,re,sys

def gaps(path, prefix,extension):
	found_numbers  = [] 
	regex = re.compile(r'0\d*.*')
	for foldername,subfolder, filename in os.walk(path):
		for name in filename:
			if name.startswith(prefix) and name.endswith('.txt'):
				suffix = regex.search(name).group()
				raw_number, ext = suffix.split('.')
				number = raw_number[2:]
				found_numbers.append(number)	
								
	ordered_numbers = sorted([int(number) for number in found_numbers])

	for i in range(1,len(ordered_numbers)+1):
		zeroes = '0' * int(len(raw_number)-len(number))
		file = prefix+zeroes+str(i)+extension
		if os.path.exists(file) == False:
			edit_num = ordered_numbers[i-1]
			zeroes = '0' * int(len(raw_number)-len(str(edit_num)))
			newName = prefix+zeroes+str(edit_num)+extension
			shutil.move(newName, file)
			print("Renamed file")

path = sys.argv[1]
prefix = sys.argv[2]
extension = sys.argv[3]
gaps(path,prefix, extension)
