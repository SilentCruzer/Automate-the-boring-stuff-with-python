# Practice Questions

**1. Does PyInputPlus come with the Python Standard Library?**

	No, PyiInputPlus is a third party module

**2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?**

	Because it helps to make our code shorter and easier to understand.

**3. What is the difference between inputInt() and inputFloat()?**

	inputInt() - returns integer value
	inputFloat() - returns float value

**4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?**

	pyip.inputint(min = 0 , max = 99)

**5. What is passed to the allowRegexes and blockRegexes keyword arguments?**

	allowRegexes - regex strings which are allowed
	blockRegexes - regex strings which are not allowed

**6. What does inputStr(limit=3) do if blank input is entered three times?**

	RetryLimitException will be given by the function

**7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?**

	It takes the input as 'hello' 
