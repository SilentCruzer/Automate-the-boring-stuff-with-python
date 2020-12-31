1. What is the protocol for sending email? For checking and receiving email?

	SMTP and IMAP

2. What four smtplib functions/methods must you call to log in to an SMTP server?

	smtplib.SMTP(), smtpobj.echlo(), smptobj.starttls(), smptobj.login()

3. What two imapclient functions/methods must you call to log in to an IMAP server?

	imapclient.IMAPClient(), imapobj.login()

4. What kind of argument do you pass to imapObj.search()?

	IMAP keywords like BEFORE 'date', FROM 'string' 

5. What do you do if your code gets an error message that says got more than 10000 bytes?

	Assign the variable imaplib.MAXLINE a large integer value

6. The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?

	pyzmail

7. When using the Gmail API, what are the credentials.json and token.json files?

	The files tells the module which google account to use.

8. In the Gmail API, what’s the difference between “thread” and “message” objects?

	A thread is a multiple emails in a conversation while message is an single email

9. Using ezgmail.search(), how can you find emails that have file attachments?

	By passing 'has:attachment' as argument to search()

10. What three pieces of information do you need from Twilio before you can send text messages?

	Twilio account SID number, authentication token number and Twilio phone number.

