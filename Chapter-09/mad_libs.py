import sys, re

replace_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
with open('mad_libs_text.txt') as f:
	sentence = f.read()

for word in replace_words:
	while(word in sentence):
		replace = input("Enter an " + word.lower() + ": " )
		sentence = sentence.replace(word, replace, 1)

print(sentence)

with open("mad_Libs_after.txt",'w') as f:
	f.write(sentence) 


