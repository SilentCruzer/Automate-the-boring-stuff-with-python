import openpyxl,os

path =''
wb = openpyxl.Workbook()
sheet = wb['Sheet']
row, column = 1,1
for foldername, subfolder, filename in os.walk(path):
	for name in filename:
		if name.endswith('.txt'):
			with open(name) as f:
				text=f.readlines()
			for string in text:
				sheet.cell(row=row,column=column).value=string
				row+=1
			row=1
			column+=1

wb.save('fromtext.xlsx')

