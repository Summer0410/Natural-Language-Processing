#########################################################
##  CS 4750 (Fall 2018), Assignment #2                 ##
##   Script File Name: reconstruct.py                  ##
##       Student Name: Linqiao Xia                     ##                                     
##              MUN #: 201446135               		   ##
#########################################################
from __future__ import division
from readFST import *
from econstruct import *
import argparse
from sets import Set
#************** A function to construct the upper form from the lower form****************8
def reconstructUpper(l,F):
	fst = readFile(F)
	lower = list(l)
	currentState = 1
	upper = ""
	for lowerLength in range (0,len(lower)-1):
		currentLower = lower[lowerLength]
		found1 = 0
		for i in range (2,len(fst)):
			if(fst[i][0]==currentState and fst[i][2]==currentLower and found1 == 0):
				upper=upper+(fst[i][3])
				currentState = fst[i][4]
				found1 = 1
	currentLower = lower[len(lower)-1]
	found = 0
	for i in range (2,len(fst)):
			if(fst[i][0]==currentState and fst[i][2]==currentLower and found==0):
				upper=upper+(fst[i][3])
				currentState = fst[i][4]
				found = 1
	print(upper)
		

#************** A function to construct the lower form from the upper form****************8

def reconstructLower(u,filename):
	fst = readFile(filename)
	upper = list(u)
	currentState = 1
	currentUpper,lower = "",""
	
	for upperLength in range (0,len(upper)-1):
		found1 = 0
		currentUpper = upper[upperLength]
		for i in range (2,len(fst)):
			if(fst[i][0]==currentState and fst[i][3]==currentUpper and found1 == 0):
				lower=lower+(fst[i][2])
				currentState = fst[i][4]
				found1 = 1
	
	currentUpper = upper[len(upper)-1]
	found = 0
	for i in range (2,len(fst)):
			if(fst[i][0]==currentState and fst[i][3]==currentUpper and found==0):
				lower=lower+(fst[i][2])
				currentState = fst[i][4]
				found = 1
	print(lower)
#**************** a function that composes 2 fsts into 1 fst*********************************8
def composeFST(F1,F2):
	fst1 = readFile(F1)
	fst2 = readFile(F2)
	state1 = int(fst1[0]["numberOfState"])
	state2 = int(fst2[0]["numberOfState"])
	composedStates,composedTransitions = [],[]
	count = 0
	for i in range(1,state1+1):
		for j in range(1,state2+1):
			composedStates.append([i,j])
	for i in range (0, len(composedStates)):
		for j in range(0,len(composedStates)):
			state11 = composedStates[i][0]
			state12 = composedStates[j][0]
			state21 = composedStates[i][1]
			state22 = composedStates[j][1]
			for p in range (2,len(fst1)):
				if(fst1[p][0] ==state11 and fst1[p][4] == state12):
					state21Input = fst1[p][3]
					for q in range (2, len(fst2)):
						currentTransition = []
						if(fst2[q][0]==state21 and fst2[q][4]==state22 and fst2[q][2] == state21Input):#check if the output from fst1 equals to an input of fst2
							count = count + 1
							currentTransition.append(composedStates[i])
							currentTransition.append("F")
							currentTransition.append(fst1[p][2])
							currentTransition.append(fst2[q][3])
							currentTransition.append(composedStates[j])
							composedTransitions.append(currentTransition)
	composedLexicals = set(fst1[1]["lexicicals"]).union(fst2[1]["lexicicals"])
	tempList = []
	tempList.append(count)
	tempList.append(composedLexicals)
	composedTransitions = tempList + composedTransitions
	# for transitions in composedTransitions:
	# 	print (transitions)
	return composedTransitions
		

#**********************Main function************************************************************8

def main():
	parser = argparse.ArgumentParser(description='Process similarity between different textfiles.')
	parser.add_argument('fileNames', metavar='N', type=str, nargs='+',help='an string for the accumulator')
	args = parser.parse_args().fileNames
	constructType = args[0]
	inputFile = args[1]
	fstFile = args[2:len(args)]
	if(len(fstFile)==1):
		fst = readFile(fstFile[0])
		print("Composed FST has %s states and %s transitions"%(fst[0]["numberOfState"],len(fst)-2))
		print("Lexical form: %s"%(fst[1]["lexicicals"]))
		f = open(inputFile, "r")
		inputArray = f.read().split("\n")

		if(constructType=="surface"):
			for i in range (1,len(inputArray)):
				print("Lexical form: %s"%(inputArray[i]))
				print("Reconstructed surface forms:")
				reconstructUpper(inputArray[i],fstFile[0])
				print("-----------------------------------------------------------")
		if(constructType=="lexical"):
			for i in range (1,len(inputArray)):
				print("Surface form: %s"%(inputArray[i]))
				print("Reconstructed lexical forms:")
				reconstructLower(inputArray[i],fstFile[0])
				print("-----------------------------------------------------------")
	else:
		fst = composeFST(fstFile[0],fstFile[1])
		f = open(inputFile, "r")
		inputArray = f.read().split("\n")
		if(constructType=="surface"):
			for i in range (1,len(inputArray)):
				print("Lexical form: %s"%(inputArray[i]))
				print("Reconstructed surface forms:")
				lower = list(inputArray[i])
				currentState = [1,1]
				upper = ""
				for lowerLength in range (0,len(lower)-1):
					currentLower = lower[lowerLength]
					found1 = 0
					for i in range (2,len(fst)):
						if(fst[i][0]==currentState and fst[i][2]==currentLower and found1 == 0):
							upper=upper+(fst[i][3])
							currentState = fst[i][4]
							found1 = 1
				currentLower = lower[len(lower)-1]
				found = 0
				for i in range (2,len(fst)):
						if(fst[i][0]==currentState and fst[i][2]==currentLower and found==0):
							upper=upper+(fst[i][3])
							currentState = fst[i][4]
							found = 1
				print(upper)
		
				print("-----------------------------------------------------------")
		if(constructType=="lexical"):
			for i in range (1,len(inputArray)):
				print("Surface form: %s"%(inputArray[i]))
				print("Reconstructed lexical forms:")
				upper = list(inputArray[i])
				currentState = [1,1]
				currentUpper,lower = "",""
				for upperLength in range (0,len(upper)-1):
					found1 = 0
					currentUpper = upper[upperLength]
					for i in range (2,len(fst)):
						if(fst[i][0]==currentState and fst[i][3]==currentUpper and found1 == 0):
							lower=lower+(fst[i][2])
							currentState = fst[i][4]
							found1 = 1
				
				currentUpper = upper[len(upper)-1]
				found = 0
				for i in range (2,len(fst)):
						if(fst[i][0]==currentState and fst[i][3]==currentUpper and found==0):
							lower=lower+(fst[i][2])
							currentState = fst[i][4]
							found = 1
				print(lower)
				print("-----------------------------------------------------------")

	
if __name__ == "__main__":
	main()

















