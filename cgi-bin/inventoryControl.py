import shelve
from inventoryObjects import *

defalutInventory = "/home/bear/Projects/inventory/Inventory"
curInventory = defalutInventory

def createInventory():
	inventory = shelve.open(defalutInventory)
	for room in rooms:
		tmp = {}
		for Type in types:
			tmp[Type] = {}
		inventory[room] = tmp
	
	inventory["Index"] = []	
	inventory.close()

def recreateInventory():
	inventory = shelve.open(defalutInventory)
	for key in inventory:
		del inventory[key]
	inventory.close()
	createInventory()


if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		print "Please provide an argument"

	elif sys.argv[1] == "createInventory":
		createInventory()
	elif sys.argv[1] == "recreateInventory":
		recreateInventory()
