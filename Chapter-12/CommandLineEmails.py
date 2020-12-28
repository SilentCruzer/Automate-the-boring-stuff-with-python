from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,time

email = 'foundmebut@gmail.com'
password = 'itsnouse123'


To = sys.argv[1]
message = sys.argv[2]

subject = 'From command line'

browser = webdriver.Chrome()
browser.get('https://accounts.google.com/signin')

mail = browser.find_element_by_name('identifier')
mail.send_keys(email)
time.sleep(1)
mail.send_keys(Keys.ENTER)


mail = browser.find_element_by_name('password')
mail.send_keys(password)
time.sleep(1)	
mail.send_keys(Keys.ENTER)


compose = browser.find_element_by_tag_name('html')
compose.send_keys('c')

to = browser.find_element_by_name('to')
to.send_keys(To)

subject_box = browser.find_element_by_class_name('subjectbox')
subject_box.send_keys(subject)

content = browser.find_element_by_class_name()
content.send_keys(message)

send = browser.find_element_by_class_name('v')
send.send_keys(Keys.ENTER)