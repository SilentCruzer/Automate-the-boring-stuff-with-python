# Practice Questions

**1. What are the two values of the Boolean data type? How do you write them?**
	
   The two types of boolean data types are : True and False

   When written in python they should start with capital T OR F and rest 
   of the words in lowercase. No uotes should be used.


**2. What are the three Boolean operators?**

   and, or, not


**3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean 
  values for the operator and what they evaluate to).**

	 Truth table of or:

	  True or True     -   True
	  True or False    -     True
	  False or True    -    True
	  False or False   -   False


	Truth table of and:
	 True and True       -  True
	 True and False      -  False
	 False and True      - False
	 False and False     - False


	Truth table of not:
	 not True             -  False
	 not False            -   True



**4. What do the following expressions evaluate to?**

	(5 > 4) and (3 == 5)		 			- False
	not (5 > 4)					 			- False
	(5 > 4) or (3 == 5)          			- True
	not ((5 > 4) or (3 == 5))    			- False
	(True and True) and (True == False)     - False
	(not False) or (not True)    			- True



**5. What are the six comparison operators?**

   == , !=, <, >, <=, >=



**6. What is the difference between the equal to operator and the assignment operator?**

   == operator asks whether two values are same.
   = operator puts the value on right into the variable in left



**7. Explain what a condition is and where you would use one.**

   Conditions always evaluate to True or False. Condition can be used in flow control statements.


**8. Identify the three blocks in this code:**

	spam = 0
	if spam == 10:
	    print('eggs')
	    if spam > 5:
	        print('bacon')
	    else:
	        print('ham')
	    print('spam')
	print('spam')

   The first block starts at print('eggs')
   The second block starts at print('bacon')
   The third block starts at print('ham')


**10. What keys can you press if your program is stuck in an infinite loop?**

   CTRL-C


**11. What is the difference between break and continue?**

   The break statement helps to exit the loop whereas continue statement jumps back to the start
   of the loop


**12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?**

	range(10)  - It starts to count from 0 and ends at 9
	range(0,10) - It starts to count from 0 and ends at 9
	range(0,10,1) - It starts to count from 0 and ends at 9
	Although the aruguments are different, the three function returns the same output.


**14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?**

	import spam
	spam.bacon()

