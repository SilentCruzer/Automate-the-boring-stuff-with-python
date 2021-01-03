import smtplib, sys, random

with open("emails.txt") as f:
	emails = f.readlines()
	emails = [mail.strip() for mail in emails]

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

user = sys.argv[1]
password = sys.argv[2]
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(user, password)

for mail in emails:
	randomChores = random.choice(chores)
	body = "Subject: You have the following chore this week: " + randomChores
	chores.remove(randomChores)
	print("sending mail to " + mail)
	smtpObj.sendmail(user, mail,body)

smtpObj.quit()