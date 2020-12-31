import smtplib, sys, random

with open("emails.txt") as f:
	emails = f.readlines()
	emails = [mail.strip() for mail in emails]

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sys.argv[1], sys.argv[2])

for mail in emails:
	randomChores = random.choice(chores)
	body = "Subject: You have the following chore this week: " + randomChores
	chores.remove(randomChores)
	print("sending mail to " + mail)
	sendmailStatus = smtpObj.sendmail(sys.argv[1], mail,body)

	if sendmailStatus != {}:
		print('There was a problem sending email to %s: %s' % (mail,sendmailStatus))

smtpObj.quit()