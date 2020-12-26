import pyinputplus as pyip
import time, random

correctanswers = 0
for ques in range(11):
	x = random.randint(0,9)
	y = random.randint(0,9)
	question = "Q-"+ str(ques) + ') ' + str(x) + 'x' + str(y) + ' = ' 
	try:
		pyip.inputStr(question, allowRegexes=['^%s$' % (x * y)],blockRegexes=[('.*', 'Incorrect!')],timeout=8, limit=3)


	except pyip.RetryLimitException:
		print("Out of tries")
		break

	except pyip.TimeoutException:
		print("Out of time")
		break

	else:
		print('correct')
		correctanswers +=1

	time.sleep(1)
print(correctanswers)
