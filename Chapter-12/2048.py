from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://play2048.co/')

game_over = browser.find_element_by_css_selector('.game-container p')
html = browser.find_element_by_css_selector('html')

while game_over.text != 'Game over!':
	html.send_keys(Keys.UP) 
	html.send_keys(Keys.RIGHT)
	html.send_keys(Keys.DOWN)
	html.send_keys(Keys.LEFT)
	