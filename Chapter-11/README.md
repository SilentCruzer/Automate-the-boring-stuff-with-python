# Practice Questions

**1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.**

	assert spam >= 10, "spam is less than 10"

**2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).**

	eggs.lower!=bacon.lower()

**3. Write an assert statement that always triggers an AssertionError.**

	assert False, "Always triggers"

**4. What are the two lines that your program must have in order to be able to call logging.debug()?**

	import logging
	logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
	%(levelname)s -  %(message)s')

**5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?**

	import logging
	logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
	format=' %(asctime)s -  %(levelname)s -  %(message)s')

**6. What are the five logging levels?**

	DEBUG, INFO, WARNING, ERROR, CRITICAL

**7. What line of code can you add to disable all logging messages in your program?**

	logging.diable(logging.CRITICAL)

**8. Why is using logging messages better than using print() to display the same message?**

	Logging messages provide timestamps and level names. All Logging messages can also be disabled with a single line of code.


**9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?**

 	Step Over button will quickly execute the function call without stepping into it , Step Out function will execute the rest pf the code until it steps out of the function. Step in fuction will move the debugger into the functio call.

**10. After you click Continue, when will the debugger stop?**

 	Till it reaches the end of the program or the breakpoint

**11. What is a breakpoint?**
	
	It is the setting of point in the code at which the debugger pauses.

**12. How do you set a breakpoint on a line of code in Mu?**

	Click the line number to make a red dot.
	


