#########################################################
##  CS 4750 (Fall 2018), Assignment #2                 ##
##   Script File Name: reconstruct.py                  ##
##       Student Name: Linqiao Xia                     ##                                     
##              MUN #: 201446135               		   ##
#########################################################

from readFST import *
import argparse

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
def composeFST(F1,F2):

def main():
	parser = argparse.ArgumentParser(description='Process similarity between different textfiles.')
	parser.add_argument('fileNames', metavar='N', type=str, nargs='+',help='an string for the accumulator')
	args = parser.parse_args().fileNames
	constructType = args[0]
	inputFile = args[1]
	fstFile = args[2:len(args)]
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
if __name__ == "__main__":
	main()

















