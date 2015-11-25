from bsddb3 import db 
import time
import datetime
from io import StringIO
import csv

# determines type of query and calls relevant function
def evaluateQuery (queryType, queryOperator, queryCond):
        
    matchingRecords = []
    
    if queryType == "p":
        matchingRecords = termsSearch ("pt.idx", queryOperator, queryCond)
    elif queryType == "r":
        matchingRecords = termsSearch ("rt.idx", queryOperator, queryCond)
    elif queryType == "pprice":
        matchingRecords = priceSearch (queryOperator, queryCond)
    elif queryType == "rscore":
        if queryOperator == "<":
            queryMin = "0.0"
            queryMax = queryCond
            matchingRecords = scoreSearch (queryMin, queryMax)
        elif queryOperator ==">":
            queryMin = queryCond
            queryMax = "inf"
            matchingRecords = scoreSearch (queryMin, queryMax)
    elif queryType == "rdate":
        matchingRecords = dateSearch (queryOperator, queryCond)
    elif queryType == "pr":
        if queryCond[-1] == "%":
            matchingRecords1 = partialTermsSearch ("pt.idx", queryOperator, queryCond)
            matchingRecords2 = partialTermsSearch ("rt.idx", queryOperator, queryCond)
            matchingRecords = matchingRecords1 + matchingRecords2
        else:
            matchingRecords1 = termsSearch ("pt.idx", queryOperator, queryCond)
            matchingRecords2 = termsSearch ("rt.idx", queryOperator, queryCond)
            matchingRecords = matchingRecords1 + matchingRecords2
        
    return(matchingRecords)
    
# finds matches for partial searches
def partialTermsSearch (fileName, queryOperator, queryCond):
    matchingRecords = []
    queryCond = queryCond[0:-1]
    queryLen = len(queryCond)
    
    termsDB = db.DB()
    termsDB.open(fileName)
    
    cursor = termsDB.cursor()
    current = cursor.first()
    while current:
        term = current[0].decode("utf-8")
        if term[0:queryLen] == queryCond:
            recordId = current[1].decode("utf-8")
            matchingRecords.append(recordId)
        current = cursor.next()     
    cursor.close()
    termsDB.close()
    
    return(matchingRecords)

# finds matches for terms in titles or review text
def termsSearch (fileName, queryOperator, queryCond):
    matchingRecords = []
    queryCond = bytes(queryCond, encoding='utf-8')
    
    termsDB = db.DB()
    termsDB.open(fileName)
    
    cursor = termsDB.cursor()
    current = cursor.set(queryCond)
    while current:
        recordId = current[1].decode("utf-8")
        matchingRecords.append(recordId)
        current = cursor.next_dup()     
    cursor.close()
    termsDB.close()
    
    return(matchingRecords)
    
# finds matches for price
def priceSearch (queryOperator, queryCond):
    matchingRecords = []
    queryCond = float(queryCond)
   
    reviewsDB = db.DB()
    reviewsDB.open("rw.idx")
    
    cursor = reviewsDB.cursor()
    current = cursor.first()
    while current:
        productPrice = getProductPrice(current[1].decode("utf-8"))
        try:
            if queryOperator == ">":
                if float(productPrice) > queryCond:
                    matchingRecords.append(current[0].decode("utf-8"))
            elif queryOperator == "<":
                if float(productPrice) < queryCond:
                    matchingRecords.append(current[0].decode("utf-8"))   
        except:
            #encountered unknown for price
            pass
        current = cursor.next()    
    cursor.close()
    reviewsDB.close()
    
    return(matchingRecords)    
    
# finds matches for scores
def scoreSearch (queryMin, queryMax):
    matchingRecords = []
    queryMin = bytes(queryMin, encoding='utf-8')
    scoresDB = db.DB()
    scoresDB.open("sc.idx")
    cursor = scoresDB.cursor()
    # how to compare ?
    current = cursor.set_range(queryMin)
    if float(current[0].decode("utf-8")) <= float(queryMin.decode("utf-8")):
        current = cursor.next()
    maxExceeded = False
    while current and not(maxExceeded):
        if float(current[0].decode("utf-8")) >= float(queryMax):
            maxExceeded = True
            continue
        recordId = current[1].decode("utf-8")
        matchingRecords.append(recordId)        
        current = cursor.next()     
    cursor.close()    
    scoresDB.close()
    
    return(matchingRecords)
    
# finds matches for date
def dateSearch (queryOperator, queryCond):
    queryCond = time.mktime(datetime.datetime.strptime(queryCond, "%Y/%m/%d").timetuple())
    matchingRecords = []
   
    reviewsDB = db.DB()
    reviewsDB.open("rw.idx")
    
    cursor = reviewsDB.cursor()
    current = cursor.first()
    while current:
        reviewDate = getReviewDate(current[1].decode("utf-8"))
        if queryOperator == ">":
            if float(reviewDate) > queryCond:
                matchingRecords.append(current[0].decode("utf-8"))
        elif queryOperator == "<":
            if float(reviewDate) < queryCond:
                matchingRecords.append(current[0].decode("utf-8"))            
        current = cursor.next()    
    cursor.close()
    reviewsDB.close()
    
    return(matchingRecords)    

# gets the date from review text
def getReviewDate (review):
    reviewFile = StringIO(review)
    reader = csv.reader(reviewFile, delimiter=',')
    for row in reader:
        return(row[7])

# gets the price from review text
def getProductPrice (review):
    reviewFile = StringIO(review)
    reader = csv.reader(reviewFile, delimiter=',')
    i = 0
    for row in reader:
        return(row[2])
    
#prints data for given reviewID
def printMatches (reviewID):
    print(reviewID)
    reviewsDB = db.DB()
    reviewsDB.open("rw.idx")   
    reviewID = bytes(reviewID, encoding='utf-8')
    cursor = reviewsDB.cursor()
    current = cursor.set(reviewID)
    print(current[1].decode("utf-8"))
    cursor.close()
    reviewsDB.close()    
