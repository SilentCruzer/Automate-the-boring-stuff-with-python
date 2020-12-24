import re

def reStrip(string, char = ' '):
	strip_format = re.compile(char)
	after_strip = strip_format.sub('',string)
	print(after_strip)

text = input("Enter text: ")
remove = input("Enter character you want to remove(leave blank to remove spaces) : ")
if remove == '':
	reStrip(text)
else:
	reStrip(text,remove)
