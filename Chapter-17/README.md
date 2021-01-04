# Practice Questions

**1. What is the Unix epoch?**

	Its is a reference moment that a program uses January 1, 1970, UTC.

**2. What function returns the number of seconds since the Unix epoch?**

	time.time()

**3. How can you pause your program for exactly 5 seconds?**

	time.sleep(5)

**4. What does the round() function return?**

	It returns the closest integer of the value passed.

**5. What is the difference between a datetime object and a timedelta object?**

	A datetime object represents a specific moment of time while timedelta represents the duration of time.

**6. Using the datetime module, what day of the week was January 7, 2019?**

	datetime.datetime(2019, 1, 7).weekday()

**7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?**

	thread = threading.Thread(target=spam)
	thread.start()

**8. What should you do to avoid concurrency issues with multiple threads?**

	Neither thread should read or write the same variable.
