import requests, bs4

url = input("Enter URL: ")
res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')

linkcount, errorcount =  0,0
flagged = []
for link in links:
	if link['href'].startswith('https'):
		try:
			res2 = requests.get(link['href'])
			res2.raise_for_status()
			linkcount +=1
		except Exception as exc:
			errorcount +=1
			flagged.append(link['href'])


total = linkcount + errorcount

print("Out of " + str(total) + " links "+ str(errorcount) + " returned 404 Not Found")
if len(flagged > 0):
	print("These are the flagged links: ")
	for link in flagged:
		print(link)