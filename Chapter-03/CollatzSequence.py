def collatz(number):
	if number%2==0:
		return number//2
	else:
		return 3 * number + 1

print("Enter a number:")
while True:
	number = int(input())
	final_number = collatz(number)
	print(final_number)
	if final_number == 1:
		break
	else:
		continue
