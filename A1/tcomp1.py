						#########################################################
						##  CS 4750 (Fall 2018), Assignment #1, Question #1    ##
						##   Script File Name: tcomp1.py                       ##
						##       Student Name: Linqiao                         ##
						##         Login Name: Xia                             ##
						##              MUN #: 201446135                       ##
						#########################################################


from __future__ import division
import argparse
import itertools

def main():
	parser = argparse.ArgumentParser(description='Process similarity between different textfiles.')
	parser.add_argument('fileNames', metavar='N', type=str, nargs='+',help='an string for the accumulator')
	args = parser.parse_args()
	masterFile = args.fileNames[0]#The master file is the first coammand argument
	n = int(args.fileNames[1])# The n value is the second command argument
	comparingTextfiles = args.fileNames[2:len(args.fileNames)]# The rest arguments are comparing files
	master= open (masterFile,"r")
	masterText = "";
	if master.mode == "r":
		masterText = master.read()#get the content of the master file
		masterText = masterText.split()
	maxSim = -1
	for i in range (0,len(comparingTextfiles)):
		comparing= open (comparingTextfiles[i],"r")
		comparingText = "";
		if comparing.mode == "r":
			comparingText = comparing.read()#get the content of the master file
			comparingText = comparingText.split()
		sim = calSim(masterText,comparingText,n)#call a function which calculates the similarity
		if (sim > maxSim):
			maxSim = comparingTextfiles[i]#Comparing the similarity of different comparing files and store the maxmun similarity file
		print("Sim(%s,%s) is %s" %(masterFile,comparingTextfiles[i],sim))
	print("File \"%s \"is most similar to file \"%s\"" %(maxSim, masterFile))


def calSim(masterFile,comparingFile, n):
	master_n_gram = calN_gram(masterFile,n)
	comparing_n_gram = calN_gram(comparingFile,n)
	diff = 0
	for i in master_n_gram:
		found = 0
		matchName = ""
		for j in comparing_n_gram:
			if (i == j):
				diff += abs(float(comparing_n_gram[j])-float(master_n_gram[i]))
				found = 1
				matchName = i
		if(matchName != ""):
			del comparing_n_gram[matchName]
		if (found == 0):
			diff += float(master_n_gram[i])
	for left in comparing_n_gram:
		diff += float(comparing_n_gram[left])

	sim =  "{0:.3f}".format(1.0 - diff/2.0)
	return sim

def calN_gram(textList,n):
	#*******************Get unique letters in the textFile***************************
	listLength = len(textList)
	stringText = ""
	for i in range (0,listLength):
		stringText += textList[i]
	charList = stringText[0];
	for i in range (1,len(stringText)):
		appeared = 0
		j = 0 
		while(appeared==0 and j<len(charList)):
			if(stringText[i]==charList[j]):
				appeared = 1
			else:
			    appeared = 0
			j+=1
		if(appeared == 0):
			charList+=stringText[i]
	#********************************Build the n-diagram ************************************************
	combinations = [''.join(x) for x in itertools.product(charList,repeat = n)]#Get the vectors occurance in the textfile
	vectors = []# declare a new list to store the vectors occurred in the text file
	for i in range (0,listLength):
		if ([len(textList[i])]>=n):
			for j in range(0,len(textList[i])-n+1):
				vectors.append(textList[i][j:j+n])#add elements to the vector list
	n_gram = {}#diclare an empty dictionary 
	for i in range (0,len(combinations)):
		count = 0
		for j in range (0,len(vectors)):
			if (combinations[i]==vectors[j]):#Check the occurance of a vector
				count+=1
		n_gram[combinations[i]] =count/len(vectors)#Create a n-gram in thedictionary
	return n_gram
		

if __name__ == "__main__":
	main()


