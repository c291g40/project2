from evaluateQueries import evaluateQuery
from evaluateQueries import printMatches

# main loop for getting queries
wantExit = False
while not(wantExit):
	
	query = input("Please enter your query: ").lower()
	if query == "exit":
		wantExit = True
		continue
	splitQuery = query.split()
	#print(splitQuery)

	# following lists store diff. condition
	matchingReviews = []
	titleCond = []
	reviewCond = []
	priceCond = []
	scoreCond = []
	dateCond = []
	reviewTitleCond = []
	
	# parse the query and separate conditions
	for term in range(len(splitQuery)):
		if "p:" in splitQuery[term]:
			titleCond.append(splitQuery[term])
			splitQuery[term] = ""
		elif "r:" in splitQuery[term]:
			reviewCond.append(splitQuery[term])
			splitQuery[term] = ""
		elif "<" in splitQuery[term] or ">" in splitQuery[term]:
			if len(splitQuery[term]) == 1:
				condition = splitQuery[term-1]+splitQuery[term]+splitQuery[term+1]
				splitQuery[term-1] = ""
				splitQuery[term] = ""
				splitQuery[term+1] = ""
			elif splitQuery[term][-1] in ["<",">"]:
				condition = splitQuery[term]+splitQuery[term+1]
				splitQuery[term] = ""
				splitQuery[term+1] = ""
			elif splitQuery[term][0] in ["<",">"]:
				condition = splitQuery[term-1]+splitQuery[term]
				splitQuery[term-1] = ""
				splitQuery[term] = ""
			else:
				condition = splitQuery[term]
				splitQuery[term] = ""
			if "pprice" in condition:
				priceCond.append(condition)
			elif "rscore" in condition:
				scoreCond.append(condition)
			elif "rdate" in condition:
				dateCond.append(condition)
			
	#store left over conditions as p&r type
	for term in splitQuery:
		if term != "":
			reviewTitleCond.append(term)

	#print("titleCond,reviewCond,priceCond,scoreCond,dateCond,reviewTitleCond")
	#print(titleCond,reviewCond,priceCond,scoreCond,dateCond,reviewTitleCond)

	# evaluate each condition and find matching records
	for cond in titleCond:
		queryType = cond[0]
		queryOperator = cond[1]
		queryCond = cond[2:]
		matchingReviews.append(evaluateQuery(queryType, queryOperator, queryCond))
	
	for cond in reviewCond:
		queryType = cond[0]
		queryOperator = cond[1]
		queryCond = cond[2:]
		matchingReviews.append(evaluateQuery(queryType, queryOperator, queryCond))
		
	for cond in priceCond:
		queryType = cond[0:6]
		queryOperator = cond[6]
		queryCond = cond[7:]
		matchingReviews.append(evaluateQuery(queryType, queryOperator, queryCond))
		
	for cond in scoreCond:
		queryType = cond[0:6]
		queryOperator = cond[6]
		queryCond = cond[7:]
		matchingReviews.append(evaluateQuery(queryType, queryOperator, queryCond))
	
	for cond in dateCond:
		queryType = cond[0:5]
		queryOperator = cond[5]
		queryCond = cond[6:]
		matchingReviews.append(evaluateQuery(queryType, queryOperator, queryCond))
		
	for cond in reviewTitleCond:
		queryType = "pr"
		queryOperator = ":"
		queryCond = cond
		matchingReviews.append(evaluateQuery(queryType, queryOperator, queryCond))

	#get list of common matching records
	#sourced from:http://stackoverflow.com/questions/10066642/how-to-find-common-elements-in-list-of-lists
	commonMatchingReviews = set(matchingReviews[0])
	for records in matchingReviews[1:]:
		commonMatchingReviews.intersection_update(records)
		
	#prints out the final list of records	
	#print(sorted(commonMatchingReviews))
	for match in sorted(commonMatchingReviews):
		printMatches(match)
		
		
