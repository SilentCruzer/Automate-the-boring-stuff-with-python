import re
def validDate(final_date):
	date_format  = re.compile(r'((\d{2})/(\d{2})/(\d{4}))')
	final_date = date_format.search(final_date)
	day = final_date.group(2)
	month = final_date.group(3)
	year  = final_date.group(4)
	month_31 = ['01','03','05','07','08','10','12']
	month_30 = ['04','06','09','11']

	if month in month_31:
		if int(day) <=31:
			pass
		else:
			print("This is not a valid date")
			return False

	elif month in month_30:
		if int(day) <=30:
			pass
		else:
			print("This is not a valid date")
			return False


	elif int(year)%4 ==0 and month == '02':
		if int(day) <=28:
			pass
		else:
			print("This is not a valid date")
			return False

	elif month == '02':
		if int(day) <=29:
			pass
		else:
			print("Thus is not a valid date")
			return False
	else:
		print("This is not a valid date")
		return False	

	print("This is a valid date")
	return True


validDate('today is like 01/01/2020')
validDate('today is like 29/02/1998') 
validDate('today is like 29/02/2024')