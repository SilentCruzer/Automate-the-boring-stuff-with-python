import pyautogui,time

print("Press enter to start")
input()
try:
	while True:
		pyautogui.move(5,0, duration=0.25)
		time.sleep(10)
except KeyboardInterrupt:
	print("Stopped")