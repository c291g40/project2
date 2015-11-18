import sys
from getWords import getWords3

# clear outfile
outFile = open("./pterms.txt",'w')
outFile.close()

filePath = "./10.txt"
f = open(filePath, 'r')
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
		
		#Implement each field
		getWords3(productTitle, str(index))

	#This reads the next line
	line = f.readline()
	#if next line is empty, it flags the end of file flag (eof) which exits the next itteration of the while loop
	if not line:
		eof=1
		
f.close()

