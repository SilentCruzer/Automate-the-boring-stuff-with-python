# Practice Questions

**1. What is []?**
	[] is a empty list with no values.

**2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam?(Assume spam contains[2, 4, 6, 8,10].)**

	spam[2] = 'hello'


For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

**3. What does spam[int(int('3' * 2) // 11)] evaluate to?**
	
	Since '3' is a string, the statement can be seen as:
	spam[33//11] which gives spam[3]
	 So the statement evalutes to value 'd'

**4. What does spam[-1] evaluate to?**

	The last element = 'd'

**5. What does spam[:2] evaluate to?**

	Returns list with values at index values 0 to 1

**For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].**

**6. What does bacon.index('cat') evaluate to?**

	returns 1

**7. What does bacon.append(99) make the list value in bacon look like?**

	[3.14, 'cat', 11, 'cat', True, 99]

**8. What does bacon.remove('cat') make the list value in bacon look like?**

	[3.14, 11, 'cat', True, 99]

**9. What are the operators for list concatenation and list replication?**

	list concatenation -   +
	List replication   -   *

**10. What is the difference between the append() and insert() list methods?**

	append() adds value at the end of a list while insert() can add the value anywhere in a list.

**11. What are two ways to remove values from a list?**

	del statement and remove() 

**12. Name a few ways that list values are similar to string values.**

	Both have indexes. 
	Both can be concatenated and replicated

**13. What is the difference between lists and tuples?**

	Lists are mutable while tuples are not. List are defined using [] and tuples are defined using ()


**14. How do you type the tuple value that has just the integer value 42 in it? **
	
	(42,)


**15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?**

	Using tuple() and list()

**16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?**

	Contains reference to values in a list.

**17. What is the difference between copy.copy() and copy.deepcopy()?**

	copy.copy() can be used to copy mutable values in a list while copy.deepcopy() can be used to copy inner lists.

 