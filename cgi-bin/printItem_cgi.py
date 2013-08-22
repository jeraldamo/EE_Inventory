#!/usr/bin/python2

import cgi
import shelve
from inventoryObjects import *
from inventoryControl import *

store = cgi.FieldStorage()

inventory = shelve.open(curInventory)
index = inventory["Index"]
if "tag" in store:
	tag = store.getvalue("tag")

	itemPath = index[tag].split(',')
	room = inventory[itemPath[0]]
	Type = room[itemPath[1]]
	item = Type[tag]

	attributes = attributeMap[itemPath[1]]

	html = """
	<html>
	<body>
	"""
	for attribute in attributes:
		html += "%s: %s<br>"%(attribute, getattr(item, attribute))
	
	html += """
	</body>
	</html>
	"""

else:
	if store.getvalue("room") == "allRooms":
		roomList = rooms
	else:
		roomList = [store.getvalue("room")]
	
	if store.getvalue("type") == "allTypes":
		typeList = types
	else:
		typeList = [store.getvalue("type")]
		
	html = """
	<html>
	<body>
	"""
		
	for r in roomList:
		room = inventory[r]
		roomPrintedFlag = False
		for t in typeList:
			attributes = attributeMap[t]
			tyype = room[t]
			if len(tyype) > 0:
				if not roomPrintedFlag:
					html += "<h1>%s</h1><hr>" %r
					roomPrintedFlag = True
				html += "<h2>%s</h2>" %t
				if "detail" in store:
					for tag in tyype:
						item = tyype[tag]
						for attribute in attributes:
							if attribute == "room":
								html += "tag: %s<br>" %tag
							else:	
								html += "%s: %s<br>"%(attribute, getattr(item, attribute))
						html += "<br><br>"
				else:
					html += "<ul>"
					for tag in tyype:
						html += "<li>%s</li>" %tag
					html += "</ul>"
	html += """
	</body>
	</html>
	"""

print 'Content-Type: text/html'
print
print html

