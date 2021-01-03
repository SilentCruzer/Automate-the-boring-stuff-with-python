import pyautogui, pyperclip, time

time.sleep(3)
pyautogui.click()
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
string=pyperclip.paste()
print(string)
	