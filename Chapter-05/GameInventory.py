def displayInventory(inventory):
	total = 0
	print("Inventory: ")
	for item in inventory:
		print(str(inventory[item]) + " " + item)
		total += inventory[item]

	print("Total number of items : " + str(total))

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inv)