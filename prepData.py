import sys

print("Welcome to the Prep Data program.")
userInput = input("Please enter the full path of the file: ")
print("file path is: %s" % userInput)
f = open(userInput, 'r')

index=1
eof = 0
line = f.readline()
while (eof == 0):

	#if we find the beginning of an item
	if ("product/productId:" in line):
		print("found productID at index %s" %index)
		index= index +1
		productID = line.split("product/productId:")[1].lstrip().split("\n")[0]
		productTitle = f.readline().split("product/title:")[1].lstrip().split("\n")[0]
		productPrice = f.readline().split("product/price:")[1].lstrip().split("\n")[0]
		rUserID = f.readline().split("review/userId:")[1].lstrip().split("\n")[0]
		rProfileName = f.readline().split("review/profileName:")[1].lstrip().split("\n")[0]
		rHelpfulness = f.readline().split("review/helpfulness:")[1].lstrip().split("\n")[0]
		rScore = f.readline().split("review/score:")[1].lstrip().split("\n")[0]
		rTime = f.readline().split("review/time:")[1].lstrip().split("\n")[0]
		#rText = f.readline().split("review/text:")[1].lstrip()
		
		print("________________BEGIN")
		print(productID)
		print(productTitle)
		print(productPrice)
		print(rUserID)
		print(rProfileName)
		print(rHelpfulness)
		print(rScore)
		print(rTime)
		#print(rText)
		print("__________________END")	

	#This reads the next line
	line = f.readline()
	#if next line is empty, it flags the end of file flag (eof) which exits the next itteration of the while loop
	if not line:
		eof=1
		

f.close()

