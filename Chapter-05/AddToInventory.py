def displayInventory(inventory):
	total = 0
	print("Inventory: ")
	for item in inventory:
		print(str(inventory[item]) + " " + item)
		total += inventory[item]

	print("Total number of items : " + str(total))



def addToInventory(inv,add_inv):
	for item in add_inv:
		if item in inv:
			inv[item] +=1
		else:
			inv[item] = 1


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)