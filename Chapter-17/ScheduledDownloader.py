import bs4, requests, os, datetime

def comic(path):
	url = 'https://xkcd.com'
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	comic = soup.select('#comic img')

	img_url = comic[0].get('src')
	imgName = os.path.basename(img_url)
	folder = []


	for folder,subfolder,filename in os.walk(path):
		for name in filename:
			folder += name
			
	if imgName not in folder:
		res2 = requests.get('http:'+img_url)
		image= open(os.path.join(path, imgName),'wb')

		for chunk in res2.iter_content(100000):
			image.write(chunk)
		print("Downloaded latest comic")
	else:
		print("Folder is up to date")

#add path of rhe folder here
path = ''
comic(path)