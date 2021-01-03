import pyautogui, time

#After executing the code, switch to google hangouts tab.

def sendMessage(name, message):
	time.sleep(3)
	search = pyautogui.locateCenterOnScreen('search.png')
	pyautogui.click(search)
	pyautogui.write(name)
	pyautogui.press('enter')
	time.sleep(1)
	#calling the locateOnScreen twice on same variable because I faced a bug where when
	#it is in the second loop it does not locate the online symbol even when it is present. 
	online = pyautogui.locateOnScreen('search.png')
	online = pyautogui.locateOnScreen('online.png')
	if online != None:
		time.sleep(1)
		pyautogui.write(message)
		send = pyautogui.locateOnScreen('send.png')
		if send == None:
			pyautogui.press('enter')
			pyautogui.press('esc')
			print('Message sent successfully to ' + name)
		else:
			print('Couldnt send message to ' + name)
	else:
		print(name + ' is offline')


#If you want to send message to more than one person, seperate the inputs with , .
names = input("Enter the names of friends that you want to send the message to : ")
names = names.split(',')
message = input("Enter the message: ")
for name in names:
	sendMessage(name, message)
	time.sleep(1)