import sys
import phase1

def main ():
	print("Welcome to the Prep Data program.")
	#userInput = input("Please enter the full path of the file: ")
	#print("file path is: %s" % userInput)
	#f = open(userInput, 'r')
	f = open("./data/10.txt", 'r')

	#clears output files if exists 
	open("./reviews.txt", 'w').close()
	open("./pterms.txt", 'w').close()
	open("./rterms.txt", 'w').close()
	open("./scores.txt", 'w').close()

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
			

			productID = replaceQuoteSlash (productID)
			productTitle = replaceQuoteSlash (productTitle)
			productPrice = replaceQuoteSlash (productPrice)
			rUserID = replaceQuoteSlash (rUserID)
			rProfileName = replaceQuoteSlash (rProfileName)
			rHelpfulness = replaceQuoteSlash (rHelpfulness)
			rScore = replaceQuoteSlash (rScore)
			rTime = replaceQuoteSlash (rTime)
			rSummary = replaceQuoteSlash (rSummary)
			rText = replaceQuoteSlash (rText)

			fullReviewList = [str(index),productID,'"'+productTitle+'"',productPrice,rUserID,'"'+rProfileName+'"',rHelpfulness,rScore,rTime,'"'+rSummary+'"','"'+rText+'"']		
			fullReview = ','.join(fullReviewList)
			phase1.makeReviewsFile(fullReview, str(index))
			phase1.makeTermsFile(productTitle, str(index), "./pterms.txt")
			phase1.makeTermsFile(rSummary+" "+rText, str(index), "./rterms.txt")
			phase1.makeScoresFile(rScore, str(index))

		#This reads the next line
		line = f.readline()
		#if next line is empty, it flags the end of file flag (eof) which exits the next itteration of the while loop
		if not line:
			eof=1
		
	f.close()

def replaceQuoteSlash (inputString):
	outputString = inputString.replace('"', '&quot;').replace('\\', '\\\\')
	return (outputString)

 
main()
