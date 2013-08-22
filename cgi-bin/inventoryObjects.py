"""
Contains all of the data structures needed
"""

class Item():
	def __init__(self, tag):
		self.tag = tag
		self.capitolAsset = None
		self.purchaseDate = PurchaseDate()
		self.brand = ""
		self.model = ""
		self.notes = ""
		
	def __getitem__(self, i):
		return getattr(self, i)

class PurchaseDate():
	def __init__(self, month=None, day=None, year=None):
		if month is None or day is None or year is None:
			self.known = False
		else:
			self.month = str(month)
			self.day = str(day)
			self.year = str(year)
			
	def getPurchaseDate(self, format="Standard"):
		if self.known:
			if format == "Standard":
				return "%s/%s/%s" %(self.month, self.day, self.year)
				
		else:
			return "Purchase Date Unknown"
			
			
types = [
"Oscilloscope",
"Function Generator",
"Power Generator",
"Multimeter",
"Spectrum Analyzer",
"Computer",
"Monitor",
"Printer",
"Furniture",
"Other"
]

rooms = [
"MWAH 60",
"MWAH 41",
"MWAH 43",
"MWAH 189",
"MWAH 171",
"MWAH 102",
"MWAH 141",
"MWAH 271",
"MWAH 291",
"MWAH 293",
"MWAH 295",
"MWAH 259",
"MWAH 391",
"MWAH 393",
"MWAH 355",
"MWAH 421"
]

computerAttributes = [
"room",
"brand",
"model",
"ram",
"processor",
"hdd",
"extraPeriphrials",
"notes",
"capitol"
]

oscilloscopeAttributes = [
"room",
"brand",
"model",
"channels",
"speed",
"notes",
"capitol"
]

functionGeneratorAttributes = [
"room",
"brand",
"model",
"speed",
"notes",
"capitol"
]

powerGeneratorAttributes = [
"room",
"brand",
"model",
"outputs",
"voltage",
"current",
"notes",
"capitol"
]

multimeterAttributes = [
"room",
"brand",
"model",
"benchtop",
"notes",
"capitol"
]

spectrumAnalyzerAttributes = [
"room",
"brand",
"model",
"speed",
"notes",
"capitol"
]

monitorAttributes = [
"room",
"brand",
"model",
"size",
"ratio",
"notes",
"capitol"
]

printerAttributes = [
"room",
"brand",
"model",
"color",
"notes",
"capitol"
]

furnitureAttributes = [
"room",
"brand",
"model",
"type",
"notes",
"capitol"
]

otherAttributes = [
"type",
"room",
"brand",
"model",
"notes",
"capitol"
]

attributeMap = {
"Computer": computerAttributes,
"Oscilloscope": oscilloscopeAttributes,
"Function Generator": functionGeneratorAttributes,
"Power Generator": powerGeneratorAttributes,
"Multimeter": multimeterAttributes,
"Spectrum Analyzer": spectrumAnalyzerAttributes,
"Monitor": monitorAttributes,
"Printer": printerAttributes,
"Furniture": furnitureAttributes,
"Other": otherAttributes
}

computerBatchHTML = """
<html>
<body>
<form name="batchComputer" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>RAM: <input type="text" name="ram"></td>
	</tr>
	<tr>
		<td>Processor: <input type="text" name="processor"></td>
	</tr>
	<tr>
		<td>HDD: <input type="text" name="hdd"></td>
	</tr>
	<tr>
		<td>Extra Periphrials: <input type="text" name="extraPeriphrials"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Computer">
</form>
</body>
</html>
"""

computerSingleHTML = """
<html>
<body>
<form name="singleComputer" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>RAM: <input type="text" name="ram"></td>
	</tr>
	<tr>
		<td>Processor: <input type="text" name="processor"></td>
	</tr>
	<tr>
		<td>HDD: <input type="text" name="hdd"></td>
	</tr>
	<tr>
		<td>Extra Periphrials: <input type="text" name="extraPeriphrials"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Computer">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""


oscilloscopeBatchHTML = """
<html>
<body>
<form name="batchOscilloscope" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Channels: <input type="text" name="channels"></td>
	</tr>
	<tr>
		<td>Speed: <input type="text" name="speed"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Oscilloscope">
</form>
</body>
</html>
"""

oscilloscopeSingleHTML = """
<html>
<body>
<form name="singleOscilloscope" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Channels: <input type="text" name="channels"></td>
	</tr>
	<tr>
		<td>Speed: <input type="text" name="speed"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Oscilloscope">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""


functionGeneratorBatchHTML = """
<html>
<body>
<form name="batchFunctionGenerator" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Speed: <input type="text" name="speed"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Function Generator">
</form>
</body>
</html>
"""

functionGeneratorSingleHTML = """
<html>
<body>
<form name="singleFunctionGenerator" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Speed: <input type="text" name="speed"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Function Generator">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""


powerGeneratorBatchHTML = """
<html>
<body>
<form name="batchPowerGenerator" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Outputs: <input type="text" name="outputs"></td>
	</tr>
	<tr>
		<td>Voltage: <input type="text" name="voltage"></td>
	</tr>
	<tr>
		<td>Current: <input type="text" name="current"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Power Generator">
</form>
</body>
</html>
"""

powerGeneratorSingleHTML = """
<html>
<body>
<form name="singlePowerGenerator" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Outputs: <input type="text" name="outputs"></td>
	</tr>
	<tr>
		<td>Voltage: <input type="text" name="voltage"></td>
	</tr>
	<tr>
		<td>Current: <input type="text" name="current"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Power Generator">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""


multimeterBatchHTML = """
<html>
<body>
<form name="batchMultimeter" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="benchtop" value="yes">Benchtop</td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Multimeter">
</form>
</body>
</html>
"""

multimeterSingleHTML = """
<html>
<body>
<form name="singleMultimeter" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="benchtop" value="yes">Benchtop</td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Multimeter">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""

spectrumAnalyzerBatchHTML = """
<html>
<body>
<form name="batchSpectrumAnalyzer" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Speed: <input type="text" name="speed"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Spectrum Analyzer">
</form>
</body>
</html>
"""

spectrumAnalyzerSingleHTML = """
<html>
<body>
<form name="singleSpectrumAnalyzer" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Speed: <input type="text" name="speed"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Spectrum Analyzer">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""


monitorBatchHTML = """
<html>
<body>
<form name="batchMonitor" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Size: <input type="text" name="size"></td>
	</tr>
	<tr>
		<td>Ratio: <input type="text" name="ratio"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Monitor">
</form>
</body>
</html>
"""

monitorSingleHTML = """
<html>
<body>
<form name="singleMonitor" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Size: <input type="text" name="size"></td>
	</tr>
	<tr>
		<td>Ratio: <input type="text" name="ratio"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Monitor">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""


printerBatchHTML = """
<html>
<body>
<form name="batchColor" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="color" value="yes">Color</td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Printer">
</form>
</body>
</html>
"""

printerSingleHTML = """
<html>
<body>
<form name="singlePrinter" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="color" value="yes">Color</td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Printer">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""


furnitureBatchHTML = """
<html>
<body>
<form name="batchFurniture" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Furniture">
</form>
</body>
</html>
"""

furnitureSingleHTML = """
<html>
<body>
<form name="singleFurniture" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Furniture">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""


otherBatchHTML = """
<html>
<body>
<form name="batchOther" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
		<td rowspan="8"><textarea rows="20" cols="10" name="tag"></textarea></td>
	</tr>
	<tr>
		<td>Type: <input type="text" name="type"></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Other">
</form>
</body>
</html>
"""

otherSingleHTML = """
<html>
<body>
<form name="singleOther" action="add_cgi.py" method="get">
<table>
	<tr>
		<td>Room: <select name="room">%s</select></td>
	</tr>
	<tr>
		<td>Type: <input type="text" name="type"></td>
	</tr>
	<tr>
		<td>Brand: <input type="text" name="brand"></td>
	</tr>
	<tr>
		<td>Model: <input type="text" name="model"></td>
	</tr>
	<tr>
		<td>Notes: <input type="text" name="notes"></td>
	</tr>
	<tr>
		<td><input type="checkbox" name="capitol" value="yes">Capitol Asset</td>
		<td><input type="submit" value="submit"></td>
	</tr>
</table>
<input type="hidden" name="type" value="Other">
<input type="hidden" name="tag" value="%s">
</form>
</body>
</html>
"""