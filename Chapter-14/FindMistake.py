import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]

max_row = sheet.rowCount
for row in range(2,max_row+1):
	if sheet.getRow(row)[0] == '':
		break
	elif int(sheet.getRow(row)[0]) * int(sheet.getRow(row)[1]) == int(sheet.getRow(row)[2]):
		continue
	else:
		print("The value of total is wrong in row",row)
		
