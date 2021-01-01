import sys,bs4,requests,os

url = 'https://imgur.com/search?q='
search_url = url + sys.argv[1]
#specify path here
path = ''
res = requests.get(search_url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
images = soup.select('.image-list-link img')

links = ['https:' + image.get('src') for image in images]

for link in links:
	try:
		res1 = requests.get(link)
		res1.raise_for_status()
		file = open(os.path.join(path, os.path.basename(link)), 'wb')
		for chunk in res1.iter_content(100000):
			file.write(chunk)
		file.close()
	except Exception:
		print("Couldn't Download")
