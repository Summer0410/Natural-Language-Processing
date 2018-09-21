						#########################################################
						##  CS 4750 (Fall 2018), Assignment #1, Question #2    ##
						##   Script File Name: tcomp2.py                       ##
						##       Student Name: Linqiao                         ##
						##         Login Name: Xia                             ##
						##              MUN #: 201446135                       ##
						#########################################################
from __future__ import division
import argparse
from sets import Set

def main():
	parser = argparse.ArgumentParser(description='Process similarity between different textfiles.')
	parser.add_argument('fileNames', metavar='N', type=str, nargs='+',help='an string for the accumulator')
	args = parser.parse_args()
	masterFilename = args.fileNames[0]
	comparingFileNames = args.fileNames[1:len(args.fileNames)]
	x = len(countTotalWords(masterFilename))
	maxSim = -1
	for i in range (0,len(comparingFileNames)):
		SD = len(countUniqueWord(masterFilename, comparingFileNames[i]))
		y = len(countTotalWords(comparingFileNames[i]))
		sim = sim =  "{0:.3f}".format(1-SD/(x+y))#call a function which calculates the similarity
		if (sim > maxSim):
			maxSim = comparingFileNames[i]#Comparing the similarity of different comparing files and store the maxmun similarity file
		print("Sim(%s,%s) is %s" %(masterFilename,comparingFileNames[i],sim))
	print("File \"%s \"is most similar to file \"%s\"" %(maxSim, masterFilename))


def countTotalWords(file):
	textFile= open (file,"r")
	textFileContent = ""
	if textFile.mode == "r":
		textFileContent = textFile.read()#get the content of the file
		textFileContent= textFileContent.split()
	uniqueWordsList = [textFileContent[0]]
	for i in range (1,len(textFileContent)):
		appeared = 0
		for j in range(0,len(uniqueWordsList)):
			if (textFileContent[i] == uniqueWordsList[j]):
				appeared = 1
		if (appeared ==0):
			uniqueWordsList.append(textFileContent[i])
	return uniqueWordsList

def countUniqueWord(masterFile, comparingFile):
	masterList = set(countTotalWords(masterFile))
	comparingList = set(countTotalWords(comparingFile))
	intersection = masterList.intersection(comparingList)
	union = masterList.union(comparingList)
	return union - intersection

		

if __name__ == "__main__":
	main()