import openpyxl,os

path ='/home/silentcruzer/Automate-the-boring-stuff-with-python/Chapter-13'
wb = openpyxl.load_workbook('before.xlsx')
sheet = wb['Sheet1']
col_size = sheet.max_column
row_size = sheet.max_row	
row,col = 1,1

while col <= col_size:
	filename = 'text' + str(col)
	file = open(filename,'w')
	while row<= row_size:
		string = sheet.cell(row=row,column=col).value
		file.write(str(string) + '\n')
		row+=1
	file.close()
	col+=1
	row=1






