#!/usr/bin/python2
"""
Adds objects to the inventory and shows
a completion notice.
"""


from inventoryObjects import *
from inventoryControl import *
import cgi
import shelve

inventory = shelve.open(curInventory)
store = cgi.FieldStorage()

Type = store.getvalue("type")
tagList = store.getvalue("tag").split('\n')
room = store.getvalue("room")

roomList = inventory[room]
typeDict = roomList[Type]
count = 0

index = inventory['Index']

for n in tagList:
	if n:
		count += 1
		tmpItem = Item(n)
		for attribute in attributeMap[Type]:
			setattr(tmpItem, attribute, store.getvalue(attribute))
		if not tmpItem.capitol:
			tmpItem.capitol = "no"
		typeDict[n] = tmpItem
		
		index[n] = room + ',' + Type
		inventory['Index'] = index
	
roomList[Type] = typeDict
inventory[room] = roomList
inventory.close()

html = """
<html>
<body>
Added %s items of type %s to %s
<a href="index_cgi.py">Return</a>
</body>
</html>
""" % (str(count), Type, room)

print 'Content-Type: text/html'
print
print html
