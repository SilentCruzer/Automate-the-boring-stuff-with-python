import ezsheets

#value of Spreadsheet_id should be the id of the url or the name of the spreadsheet
Spreadsheet_id = ''	
ss = ezsheets.Spreadsheet(Spreadsheet_id)
sheet = ss[0]
response = sheet.getColumn('C')
for email in response:
	if email != '':
		print(email)