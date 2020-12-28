1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.

	webbrowser module uses open() function to open web browsers to a specific URL. requests module can download files and pages	 from the web. bs4 module helps to parse the HTML. selenium modules can launch and control the browsers


2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?

	reuest.get() returns a Response object. We can get the downloaded attribute as a string with the text attribute.


3. What requests method checks that the download worked?

	We can use raise_for_status() method to check if the download has worked.


4. How can you get the HTTP status code of a requests response?

	From the status_code attribute.


5. How do you save a requests response to a file?

	By opening a file in write mode and using a loop to iterate the Response object's iter_content() method to write to the file.


6. What is the keyboard shortcut for opening a browser’s developer tools?

	F12


7. How can you view (in the developer tools) the HTML of a specific element on a web page?

	Right click the element and select inspect element.


8. What is the CSS selector string that would find the element with an id attribute of main?

	'#main'


9. What is the CSS selector string that would find the elements with a CSS class of highlight?

	'.highlight'  


10. What is the CSS selector string that would find all the <div> elements inside another <div> element?

	'div div'


11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?

	'button[value="favorite"]'


12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?

	spam.getText()


13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?

	linkElem.attrs


14. Running import selenium doesn’t work. How do you properly import the selenium module?

	from selenium import webdriver


15. What’s the difference between the find_element_* and find_elements_* methods?

	find_element_* returns the first matching element while find_elements_* returns list of all the matches


16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys? 

	click() and send_keys()
	

17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?

	We can use submit()


18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?

	By using forward(), back() and refresh()

