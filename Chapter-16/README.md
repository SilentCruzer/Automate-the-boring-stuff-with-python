# Practice Questions

**1. What are some features Excel spreadsheets have that CSV spread-sheets don’t?**

	All values in a CSV file are strings, doesn't have font color or size, doesn't have worsheets, can't specify cell widths and heights, can't merge cells, can't have images or charts

**2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?**

	Pass a file object obtained from open()

**3. What modes do File objects for reader and writer objects need to be opened in?**

	In read-binary (rb) and write-binary (wb)

**4. What method takes a list argument and writes it to a CSV file?**

	writerow()

**5. What do the delimiter and lineterminator keyword arguments do?**

	delimiter changes the string that sperates the cells in a row while lineterminator changes the string that seperate rows 	

**6. What function takes a string of JSON data and returns a Python data structure?**

	json.loads()

**7. What function takes a Python data structure and returns a string of JSON data?**

	json.dumps()
