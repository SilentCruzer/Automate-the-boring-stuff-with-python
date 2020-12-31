import PyPDF2

with open('dictionary.txt') as f:
	passwords = f.readlines()
	passwords = [pwd.strip() for pwd in passwords]

#Name of the pdf file should be given and should be in current working directory

filename = ''
pdfobj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfobj)

if pdfReader.isEncrypted:
	for word in passwords:
		try:
			if pdfReader.decrypt(word) == 1:
				print('Hacked password')
				break
			elif pdfReader.decrypt(word.lower) ==1:
				print('Hacked password')
				break
		except:
			continue