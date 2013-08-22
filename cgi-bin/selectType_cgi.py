#!/usr/bin/python2

from inventoryObjects import *
import cgi

store = cgi.FieldStorage()

if "tag" in store:
	htmlTypes = ""
	for Type in types:
		htmlTypes += "<option name=%s>%s</option>\n" %(Type, Type)

	html = """
	<html>
	<body>
	<form name="printOptions" action="input_cgi.py" method="get">
	Type of asset: <select name="type">
	%s
	</select>
	<input type="hidden" name="tag" value="%s">
	<input type="submit" value="Submit">
	</form>
	</body>
	</html>
	""" % (htmlTypes, store.getvalue("tag"))

else:
	htmlTypes = ""
	for Type in types:
		htmlTypes += "<option name=%s>%s</option>\n" %(Type, Type)

	html = """
	<html>
	<body>
	<form name="printOptions" action="batchInput_cgi.py" method="get">
	Type of asset: <select name="type">
	%s
	</select>
	<input type="submit" value="Submit">
	</form>
	</body>
	</html>
	""" % htmlTypes

print 'Content-Type: text/html'
print
print html