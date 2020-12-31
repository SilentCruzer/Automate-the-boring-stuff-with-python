import PyPDF2,os

def encrypt(name):
	pdfobj = open(name, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfobj)
	pdfwriter = PyPDF2.PdfFileWriter()

	for page in range(pdfReader.numPages):
		copy = pdfReader.getPage(page)
		pdfwriter.addPage(copy)

	new_name = name[:-4] +'_encrypted.pdf'
	pdfwriter.encrypt('swordfish')
	new_pdf = open(new_name,'wb')
	pdfwriter.write(new_pdf)

	new_pdf.close()
	pdfobj.close()

	decrypt = PyPDF2.PdfFileReader(open(new_name, 'rb'))
	decrypt.decrypt('swordfish')

	if decrypt.getPage(0):
		print(new_name + ' decrypted')
	else:
		print("could not decrypt "+ new_name)

path = ''

for foldername,subfolder,filename in os.walk(path):
	for name in filename:
		if name.endswith('.pdf'):
			encrypt(name)