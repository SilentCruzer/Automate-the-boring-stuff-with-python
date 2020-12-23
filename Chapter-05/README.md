1. What does the code for an empty dictionary look like?

	spam = {}

2. What does a dictionary value with a key 'foo' and a value 42 look like?

	items = {'foo':42}

3. What is the main difference between a dictionary and a list?

	Values in list are ordered whereas values in dictionary are not.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

	We will get a KeyError

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

	No difference, both expressions checks whether the value 'cats' exists  as a key in the dictionary.


6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

	The expresiion 'cat' in spam checks whether a key named 'cat' exists whereas 'cat' in spam.values() checks if a value 'cat' exists
	for any keys in the dictionary.


7. What is a shortcut for the following code?

	if 'color' not in spam:
    	spam['color'] = 'black' 

    
       spam.setdefault('color','black')


8. What module and function can be used to “pretty print” dictionary values?

	pprint module
	pprint() function

	pprint.pprint()


