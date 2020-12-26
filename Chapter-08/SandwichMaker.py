import pyinputplus as pyip

bread_prices = {"wheat" : 75, "white": 80,"sourdough" : 90}
protein_prices = {"chicken" : 150 , "turkey" : 125 , "ham" : 125 ,"tofu" : 100}
cheese_prices = {"cheddar" : 50, "Swiss" : 80 , "mozzarella" : 75}
dressing_prices = {"mayo": 30 , "mustard" : 25 , "lettuce" : 20 , "tomato" : 20}

print("What type of bread do you want? ")
bread = pyip.inputMenu(["wheat","white","sourdough"])

print("What type of protein do you want?")
protein = pyip.inputMenu(["chicken","turkey","ham","tofu"])	

print("Do you want cheese?")
response_cheese = pyip.inputYesNo()

print("Do you want any dressings?")
response_dressing = pyip.inputYesNo()



total_price = bread_prices[bread] + protein_prices[protein]
if response_cheese == 'yes':
	print("Which cheese do you want?")
	cheese = pyip.inputMenu(["cheddar","Swiss","mozzarella"])
	total_price += cheese_prices[cheese]

if response_dressing == 'yes':
	print("Which Dressing do you want?")
	dressing = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"])
	total_price += dressing_prices[dressing]


print("The total price of sandwich is :",total_price)