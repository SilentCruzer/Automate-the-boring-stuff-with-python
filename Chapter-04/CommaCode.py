def print_strings(list):
	for i in range(0,len(list)):
		if i == len(list)-1:
				print('and', list[i])
		else:
			print(list[i], end=',')
	
spam = ['apples', 'bananas', 'tofu', 'cats']
print_strings(spam)