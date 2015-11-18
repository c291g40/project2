# Mustafa Abbasi

import re

# This function makes/opens a file called "pterms.txt" and
# writes all terms with length >= 3, along with their recordId.
# Terms consist of consecutive chars of type: [0-9a-zA-Z_].

def getWords3 (fullString, recordId):

	# tries to open the file to append
	try:
		fileOut = open("./pterms.txt",'a')
	except:
		print("Failed to open file.")
		exit()
	
	# converts string to char list for parsing
	charList = list(fullString)
	
	# iterates over string and appends valid terms to file
	appendString = ""
	for char in charList:
		if re.match(r"[\w]+", char): # check character class
			char = char.lower()
			appendString = appendString + char
		else:
			if len(appendString) >= 3:
				fileOut.write(appendString + "," + recordId + "\n")
			appendString = ""
	
	fileOut.close()
