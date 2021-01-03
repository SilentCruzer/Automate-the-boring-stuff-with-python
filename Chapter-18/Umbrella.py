import requests, bs4, re
from twilio.rest import Client

def rain():
	res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.789690000000064&lon=-122.39571499999994')
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	weather = soup.find_all(class_='col-sm-10 forecast-text')[0]
	regex = re.compile('rain')
	word = regex.search(str(weather))
	if word is None:
		return False	
	else:
		return True

def text():
	accountSID = ''
	authToken  = ''
	twilioCli = Client(accountSID, authToken)
	myTwilioNumber = ''
	myCellPhone = ''
	message = twilioCli.messages.create(body='Its going to rain today', from_=myTwilioNumber, to=myCellPhone)


if rain():
	text()