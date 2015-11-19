import sys

print("Welcome to the Prep Data program.")
#userInput = input("Please enter the full path of the file: ")
#print("file path is: %s" % userInput)
#f = open(userInput, 'r')
f = open("./data/10.txt", 'r')
index=0
eof = 0
line = f.readline()
while (eof == 0):

	#if we find the beginning of an item
	if ("product/productId:" in line):
		#increment index
		index= index +1
		#parse each field
		productID = line.split("product/productId:")[1].lstrip().split("\n")[0]
		productTitle = f.readline().split("product/title:")[1].lstrip().split("\n")[0]
		productPrice = f.readline().split("product/price:")[1].lstrip().split("\n")[0]
		rUserID = f.readline().split("review/userId:")[1].lstrip().split("\n")[0]
		rProfileName = f.readline().split("review/profileName:")[1].lstrip().split("\n")[0]
		rHelpfulness = f.readline().split("review/helpfulness:")[1].lstrip().split("\n")[0]
		rScore = f.readline().split("review/score:")[1].lstrip().split("\n")[0]
		rTime = f.readline().split("review/time:")[1].lstrip().split("\n")[0]
		rSummary = f.readline().split("review/summary:")[1].lstrip().split("\n")[0]
		rText = f.readline().split("review/text:")[1].lstrip().split("\n")[0]
		
		#printout for debugging
		if __debug__:
			print("________________BEGIN")
			print(index)
			print(productID)
			print(productTitle)
			print(productPrice)
			print(rUserID)
			print(rProfileName)
			print(rHelpfulness)
			print(rScore)
			print(rTime)
			print(rSummary)
			print(rText)
			print("__________________END")	
		
		#Implement each field
		#makeReviewFile()
		#makePtermFile()
		#makeRtermFile()
		#makeScoreFile()

	#This reads the next line
	line = f.readline()
	#if next line is empty, it flags the end of file flag (eof) which exits the next itteration of the while loop
	if not line:
		eof=1
		
f.close()

