import requests, bs4, webbrowser,sys
import imapclient,imaplib,pprint, pyzmail


email = sys.argv[1]
password = sys.argv[2]
unsubscibe = []
imaplib.MAXLINE = 1000000

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(email , password)
imapObj.select_folder('INBOX',readonly=True)


search_all = imapObj.search(['ALL'])
for uid in search_all:
	raw_messages = 	imapObj.fetch(uid, ['BODY[]'])
	message = pyzmail.PyzMessage.factory(raw_messages[uid][b'BODY[]'])
	if message.html_part != None:
		html = message.html_part.get_payload().decode(message.html_part.charset)
	else:
		continue

	soup =  bs4.BeautifulSoup(html, 'html.parser')
	links = soup.select('a')

	for link in links:
		if 'unsubscribe' in str(link):
			new_link = link.get('href')
			unsubscibe.append(new_link)

imapObj.logout()

for link in unsubscibe:
	print('Opening links....')
	webbrowser.open(link)	

			