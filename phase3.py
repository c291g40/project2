def main ():
	
	wantExit = False
	while not(wantExit):
		
		query = input("Please enter your query: ").lower()
		if query == "exit":
			wantExit = True
			continue
		splitQuery = query.split()
		print(splitQuery)
		queries = []
		conditionsList = ["p:","r:","pprice","rscore","rdate"]
		titleCond = []
		reviewCond = []
		list3 = []
		reviewTitleCond = []
		
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
				list3.append(condition)

		for term in splitQuery:
			if term != "":
				reviewTitleCond.append(term)

		print(titleCond,reviewCond,list3,reviewTitleCond)
		
main()
