def readFile(file):
	with open(file) as f:
		content = f.readlines()
	#store states and transitions in a dictionary
	numberOfState = content[0].split(" ")[0]#number of states
	lexicical = content[0].split(" ")[1]#lexicicals
	fst,states,isFinal = [],[],[]# A list to store states
	fst.append({"numberOfState":numberOfState})
	fst.append({"lexicicals":lexicical})
	for i in range (1,len(content)):
		currentLine = content[i].split(" ")
		if (currentLine[0]!=""):
			states.append(currentLine[0])
			isFinal.append(currentLine[1])
		currentState = states[len(states)-1]
		nextState,upper,lower,isFinalState = "","","","false"
		isFinalState = list(isFinal[len(isFinal)-1])[0]
		currentDic = []
		if(currentLine[0]==""):
			lower,upper,nextState = currentLine[1],currentLine[2],int(currentLine[3])
			currentDic = [int(currentState),isFinalState,lower,upper,nextState]
			fst.append(currentDic)
	print "composed FST has %s states and %s transitions"%(fst[0]["numberOfState"],len(fst))
	print "lexicical form: %s"%(fst[1]["lexicicals"])
	return fst


  





