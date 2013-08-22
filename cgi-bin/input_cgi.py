#!/usr/bin/python2

from inventoryObjects import *
import cgi

store = cgi.FieldStorage()
		
htmlRooms = ""
for room in rooms:
		htmlRooms += "<option name=%s>%s</option>\n" %(room, room)

html = {
	"Oscilloscope": oscilloscopeSingleHTML,
	"Function Generator": functionGeneratorSingleHTML,
	"Power Generator": powerGeneratorSingleHTML,
	"Multimeter": multimeterSingleHTML,
	"Spectrum Analyzer": spectrumAnalyzerSingleHTML,
	"Computer": computerSingleHTML,
	"Monitor": monitorSingleHTML,
	"Printer": printerSingleHTML,
	"Furniture": furnitureSingleHTML,
	"Other": otherSingleHTML
}.get(store.getvalue("type")) %(htmlRooms, store.getvalue("tag"))

print 'Content-Type: text/html'
print
print html
