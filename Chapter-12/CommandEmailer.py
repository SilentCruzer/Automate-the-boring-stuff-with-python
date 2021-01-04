from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,time

mail_id = sys.argv[1]
password= sys.argv[2]

to_mail = input("Enter recipient: ")
subject = input("Enter subject: ")
message = input("Enter message: ")

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

enter_mail = browser.find_element_by_name('identifier')
enter_mail.send_keys(mail_id)
enter_mail.send_keys(Keys.ENTER)

enter_pass = browser.find_element_by_name('password')
enter_pass.send_keys(password)
enter_pass.send_keys(Keys.ENTER)
time.sleep(3)

compose = browser.find_element_by_class_name('z0')
compose.click()

enter_to = browser.find_element_by_name('to')
enter_to.send_keys(to_mail)

subject = browser.find_element_by_name('subjectbox')
subject.send_keys(subject)			

body = browser.find_element_by_class_name('Am Al editable LW-avf tS-tW')
body.send_keys(message + Keys.TAB + Keys.ENTER)

