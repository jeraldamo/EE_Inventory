#!/usr/bin/python2
"""
index_cgi.py
Main page presented to user.
Gives options:
 - Add a single item
 - Retrieve a single item
 - Add items in batch
 - Retrieve items in batch based
   on room and/or type
"""

import cgi
import shelve
from inventoryObjects import *
from inventoryControl import *

store = cgi.FieldStorage()

if "tag" in store:
	inventory = shelve.open("Inventory")
	index = inventory["Index"]
	tag = store.getvalue("tag")
	
	if tag in index:
		html = """
		<html>
		<head>
		<meta HTTP-EQUIV="REFRESH" content="0; url=printItem_cgi.py?tag=%s">
		</head>
		<body>
		
		</body>
		</html>
		"""%tag
	else:
		html = """
		<html>
		<head>
		<meta HTTP-EQUIV="REFRESH" content="0; url=selectType_cgi.py?tag=%s">
		</head>
		<body>
		
		</body>
		</html>
		"""%tag
	
elif "option" in store:
	html = """
	<html>
	<body>
	Got an option!
	</body>
	</html>
	"""
	
else:
	htmlTypes = ""
	htmlRooms = ""
	for Type in types:
		htmlTypes += "<option name=%s>%s</option>\n" %(Type, Type)
		
	for room in rooms:
		htmlRooms += "<option name=%s>%s</option>\n" %(room, room)
	
	html = """
	<html>
	<body>
	<h1>Add Item to Inventory</h1>
	<h3>or retrieve an existing item</h3>
	<form name="input" target="_parent" action="index_cgi.py" method="get">
	Asset ID: <input type="text", name="tag">
	</form>
	<a href="selectType_cgi.py">Generate Batch Input</a>
	<hr>
	<h1>Print Inventory</h1>
	<form name="printOptions" action="printItem_cgi.py" method="get">
	<select name="type">
	<option value="allTypes">All Types</option>
	%s
	</select>
	in
	<select name="room">
	<option value="allRooms">All Rooms</option>
	%s
	</select>
	<input type="checkbox" name="detail" value="yes">Detailed
	<br><br>
	<input type="submit" value="Print">
	</form>

	<hr>

	<h1>Manage Inventory</h1>
	<a href="takeInventory_cgi.py">Take Inventory</a><br>
	<a href="../Inventory">Download Inventory</a><br>
	
	</body>
	</html>
	""" %(htmlTypes, htmlRooms)

print 'Content-Type: text/html'
print
print html
