import time, pyperclip

print("Press enter to start the stopwatch")
input()
print("Started")
startTime = time.time()
lastTime = startTime
lapNum=1

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime,2)
		totalTime = round(time.time() - startTime,2)
		watch = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).center(7), str(lapTime).rjust(5))
		print(watch)
		lapNum+=1
		lastTime = time.time()
except KeyboardInterrupt:
	print("\nDone")