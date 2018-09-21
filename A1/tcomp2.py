						#########################################################
						##  CS 4750 (Fall 2018), Assignment #1, Question #2    ##
						##   Script File Name: tcomp2.py                       ##
						##       Student Name: Linqiao                         ##
						##         Login Name: Xia                             ##
						##              MUN #: 201446135                       ##
						#########################################################

####################################### HOW TO RUN THE SCRIPT###################################################################
## enter command argument to run the script. The script takes first argument as master file name and takes the second argument ## as n value. The rest arguments will be taken as comparing files .
## ie: if you wanna find the similarities of file 1 and master file and file 2 and master file with n = 3.                    ## Enter pyhton tcomp1.py 3 file1 file 2 to run the script.
###############################################################################################################################
from __future__ import division
import argparse
from sets import Set
################## main function ##############################################################################################
def main():
	parser = argparse.ArgumentParser(description='Process similarity between different textfiles.')
	parser.add_argument('fileNames', metavar='N', type=str, nargs='+',help='an string for the accumulator')
	args = parser.parse_args()
	masterFilename = args.fileNames[0]
	comparingFileNames = args.fileNames[1:len(args.fileNames)]
	x = len(countTotalWords(masterFilename))
	maxSim = -1
	holder = ""
	for i in range (0,len(comparingFileNames)):#Using loop to calculate the similarities
		SD = len(countUniqueWord(masterFilename, comparingFileNames[i]))
		y = len(countTotalWords(comparingFileNames[i]))
		sim = sim =  "{0:.3f}".format(1-SD/(x+y))#call a function which calculates the similarity
		if (sim > maxSim):
			maxSim = sim
			holder = comparingFileNames[i]#Comparing the similarity of different comparing files and store the maxmun similarity file
		print("Sim(%s,%s) is %s" %(masterFilename,comparingFileNames[i],sim))
	print("File \"%s \"is most similar to file \"%s\"" %(holder, masterFilename))#print out the max similarity file name

#################3 A function returns the number of differnet total different words occurred in a file ################3
def countTotalWords(file):
	textFile= open (file,"r")# open the file
	textFileContent = ""
	if textFile.mode == "r":# check if the file is open successfully 
		textFileContent = textFile.read()#get the content of the file
		textFileContent= textFileContent.split() #split the file into words
	uniqueWordsList = [textFileContent[0]]# initialize a list to store the words
	for i in range (1,len(textFileContent)):
		appeared = 0
		for j in range(0,len(uniqueWordsList)):#loop through the list to check if the words has apeared in the list
			if (textFileContent[i] == uniqueWordsList[j]):
				appeared = 1
		if (appeared ==0):
			uniqueWordsList.append(textFileContent[i])# Store the word if it has not appeared in the list
	return uniqueWordsList
##################### A function to count the number of unique words in file ##############################################
def countUniqueWord(masterFile, comparingFile):
	masterList = set(countTotalWords(masterFile)) # store  master file words in a set 
	comparingList = set(countTotalWords(comparingFile)) # store comparing file words in a set
	intersection = masterList.intersection(comparingList)# calculate the words appeared in both file 
	union = masterList.union(comparingList)#calculate the union
	return union - intersection# calculate the total unique words in master file and comparing file

if __name__ == "__main__":
	main()