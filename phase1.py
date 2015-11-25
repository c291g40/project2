import re

def makeReviewsFile (fullReview, recordId):

	# tries to open the file to append
	try:
		fileOut = open("./reviews.txt",'a')
	except:
		print("Failed to open file.")
		exit()
	
	# appends fullReview to file
	fileOut.write(fullReview + "\n")
	
	# close file
	fileOut.close()


# This function makes/opens a file and writes all terms 
# from fullString with length >= 3, along with their recordId.
# Terms consist of consecutive chars of type: [0-9a-zA-Z_].

def makeTermsFile (fullString, recordId, fileName):

	# tries to open the file to append
	try:
		fileOut = open(fileName,'a')
	except:
		print("Failed to open file.")
		exit()
	
	# converts string to char list for parsing
	charList = list(fullString)
	charList.append("$") # add extra char so last term is output
	
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
	
	# close file
	fileOut.close()


def makeScoresFile (scoreString, recordId):

	# tries to open the file to append
	try:
		fileOut = open("./scores.txt",'a')
	except:
		print("Failed to open file.")
		exit()
	
	# writes to the file
	fileOut.write(scoreString + "," + recordId + "\n")
	
	# close file
	fileOut.close()
