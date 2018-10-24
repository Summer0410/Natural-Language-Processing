from readFST import *

def reconstructUpper(l,F):
	fst = readFile(F)
	lower = list(l)
	print(lower)
	currentState = 1
	upper = ""
	for lowerLength in range (0,len(lower)-1):
		currentLower = lower[lowerLength]
		for i in range (2,len(fst)):
			if(fst[i][0]==currentState and fst[i][2]==currentLower):
				print "i:%s"%(i)
				print"currentState%s"%(fst[i][0])
				print"lower:%s"%(fst[i][2])
				print"upper:%s"%(fst[i][3])
				
				upper=upper+(fst[i][3])
				currentState = fst[i][4]
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

def main:
	lowerArray = [potPs,podPs,poSPs,poZPs,SopPs,ZopPs,doPs,dopPs,bosPs,bots,bodz,boSes,boZes,bozes]
	upperArray = [pots,podz,poSes,poSes,poZes,Sops,Zops,doz,dops,bots,bodz,boSes,boZes,boses,bozes]
	reconstructUpper("dops","vcePlu.fst")















	
