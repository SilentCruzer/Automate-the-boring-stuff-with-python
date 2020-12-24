import re

def validPassword(password):
	format_upper = re.compile(r'[A-Z].*')
	format_lower = re.compile(r'[a-z].*')
	format_number = re.compile(r'[0-9].*') 	
	if len(password) < 8 :
		return False
	
	if not format_upper.search(password):
		return False

	if not format_lower.search(password):
		return False

	if not format_number.search(password):
		return False

	return True

password  = input("Enter password: ")
if validPassword(password):
	print("This is a strong password")
else:
	print("This is not a strong password")
