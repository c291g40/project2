import filecmp
import prepData

fileName = input("Enter the name of the input file (10, 1k, 10k, 100k): ")
testFile = "./data/"+fileName+"/"+fileName+".txt"
testDir = "./data/"+fileName+"/"

prepData.main(testFile)

reviewsCompare = filecmp.cmp("./reviews.txt", testDir+"reviews.txt")
ptermsCompare = filecmp.cmp("./pterms.txt", testDir+"pterms.txt")
rtermsCompare = filecmp.cmp("./rterms.txt", testDir+"rterms.txt")
scoresCompare = filecmp.cmp("./scores.txt", testDir+"scores.txt")


print("reviews.txt is same:",reviewsCompare)
print("pterms.txt is same:",ptermsCompare)
print("rterms.txt is same:",rtermsCompare) 
print("scores.txt is same:",scoresCompare)
