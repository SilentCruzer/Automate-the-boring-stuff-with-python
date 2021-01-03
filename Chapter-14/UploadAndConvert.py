import ezsheets,sys
import pyinputplus as pyip

filename = sys.argv[1]
ss = ezsheets.upload(filename)
print("Which format should the file be converted to: ")
file_format = pyip.inputMenu(["excel","ods", "csv","tsv", "pdf","html"])

if file_format == "excel":
	ss.downloadAsExcel()
	print("Downloaded excel file")

elif file_format == "ods":
	ss.downloadAsODS()
	print("Downloaded ods file")

elif file_format == "csv":
	ss.downloadAsCSV()
	print("Downloaded csv file")

elif file_format == "tsv":
	ss.downloadAsTSV()
	print("Downloaded tsv file")

elif file_format == "pdf":
	ss.downloadAsPDF()
	print("Downloaded pdf file")

else:
	ss.downloadAsHTML()
	print("Downloaded html file")


