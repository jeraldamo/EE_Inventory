#!/usr/bin/python2

from inventoryObjects import *
import cgi

store = cgi.FieldStorage()
		
htmlRooms = ""
for room in rooms:
		htmlRooms += "<option name=%s>%s</option>\n" %(room, room)


html = {
	"Oscilloscope": oscilloscopeBatchHTML,
	"Function Generator": functionGeneratorBatchHTML,
	"Power Generator": powerGeneratorBatchHTML,
	"Multimeter": multimeterBatchHTML,
	"Spectrum Analyzer": spectrumAnalyzerBatchHTML,
	"Computer": computerBatchHTML,
	"Monitor": monitorBatchHTML,
	"Printer": printerBatchHTML,
	"Furniture": furnitureBatchHTML,
	"Other": otherBatchHTML
}.get(store.getvalue("type")) %htmlRooms
	

print 'Content-Type: text/html'
print
print html
