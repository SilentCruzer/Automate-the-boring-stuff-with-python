#Pratice Questions

**1. Which of the following are operators, and which are values?**

	a) * 		- operator
	b)'hello'   - value
	c)-88.8  	- value
	d)-      	- operator
	e)/     	- operator
	f)+			- operator
	g)5	 		- value


**2. Which of the following is a variable, and which is a string?**

 spam		- variable
'spam'		- string


**3. Name three data types.**

   integers, floating point numbers, strings



**4. What is an expression made up of? What do all expressions do?**

   Expressions consist of values and operators and can evaluate down to single value.



**5. This chapter introduced assignment statements, like spam = 10. What is the difference between
  an expression and a statement?**

  An expression consist of values and functions which can evaluate to something, whereas 
  a statement is a unit of execution which dosen't retue anything.



**6. What does the variable bacon contain after the following code runs?**
	
	bacon = 20
	bacon + 1

   The variable bacon containss the value 21



**7. What should the following two expressions evaluate to?**

    'spam' + 'spamspam'
    'spam' * 3

   Both the expressions gives the same output:
   'spamspamspam'


**8. Why is eggs a valid variable name while 100 is invalid?**

   A variable name should not begin with numbers


**9. What three functions can be used to get the integer, floating-point number, or string version of a value?**
	
   int(),float(),string()


**10. Why does this expression cause an error? How can you fix it?**

    'I have eaten ' + 99 + ' burritos.'

   We cannot concatenate integer to a string.
   We can fix it by using str():

   'I have eaten ' + str(99) + ' burritos.'