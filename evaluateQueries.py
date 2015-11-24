from bsddb3 import db 
import time
import datetime
from io import StringIO
import csv

def evaluateQuery (queryType, queryOperator, queryCond):
        
    if queryType == "p":
        matchingRecords = termsSearch ("pt.idx", queryOperator, queryCond)
    elif queryType == "r":
        matchingRecords = termsSearch ("rt.idx", queryOperator, queryCond)
    elif queryType == "pprice":
        pass
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
        pass
    elif queryType == "pr":
        matchingRecords1 = termsSearch ("pt.idx", queryOperator, queryCond)
        matchingRecords2 = termsSearch ("rt.idx", queryOperator, queryCond)
        matchingRecords = matchingRecords1 + matchingRecords2
        
    return(matchingRecords)
    
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
    
def priceSearch ():
    queryCond = time.mktime(datetime.datetime.strptime(queryCond, "%d/%m/%Y").timetuple())
    matchingRecords = []
   
    reviewsDB = db.DB()
    reviewsDB.open("rw.idx")
    
    cursor = reviewsDB.cursor()
    current = cursor.first()
    while current:
        productPrice = getProductPrice(current[1].decode("utf-8"))
        if queryOperator == ">":
            if float(productPrice) > queryCond:
                matchingRecords.append(current[0].decode("utf-8"))
        elif queryOperator == "<":
            if float(productPrice) < queryCond:
                matchingRecords.append(current[0].decode("utf-8"))            
        current = cursor.next()    
    cursor.close()
    reviewsDB.close()
    
    return(matchingRecords)    
    
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
    
def dateSearch (queryOperator, queryCond):
    queryCond = time.mktime(datetime.datetime.strptime(queryCond, "%d/%m/%Y").timetuple())
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

def getReviewDate (review):
    reviewFile = StringIO(review)
    reader = csv.reader(f, delimiter=',')
    return(reader[7])

def getProductPrice (review):
    reviewFile = StringIO(review)
    reader = csv.reader(f, delimiter=',')
    return(reader[2])