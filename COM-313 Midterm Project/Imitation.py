#Griffin McAlinden
from Individual import Node
from Generation import Generation
from random import *
from Info import *

#HOW TO USE:
	#imitation(generation, e) can be used to calculate the results of each node 
	 #"imitating" its neighbors. The payouts are calculated then, based on the
	 #higher value, a winner is chosen. The results are recorded in a list 'winList'
	 #that is returned at the end of the method. 'generation' should a variable of the
	 #class Generation that contains the nodes you want to simulate. Use 'e' to change
	 #the chance of the loser to be recorded instead of the winner in winList. 'e' can
	 #be a value between 0 and 1 and the function makes a "mistake" when a randomized
	 #number between 0 and 1 is less than 'e'

	#imitateUpdate(generation, winList) updates the nodes in generation so their 
	 #type matches the results recorded in 'winList'. 'winList' should be the list
	 #returned from 'imitation' and 'generation' should be the same variable used in
	 #'imitation'


#Returns a list of the "winning" type for each node
def imitation(generation, e):
    winnerList = [] 
    pList = []
    #for i in range(generation.length+1):
       # print(generation.nList[i].pos, end = " ")
    #print(" ")
    for i in generation.nList:
        altPayout = 0
        altCount = 0
        egoPayout = 0
        egoCount = 0
        

        leftiT = i.left.iType
        iType =i.iType
        rightiT = i.right.iType

        lPayout = i.left.payout
        payout = i.payout
        rPayout = i.right.payout

        #Check payout of node and node's neighbors
        if leftiT == 0:
            altPayout = altPayout + lPayout
            altCount = altCount +1
        else:
            egoPayout = egoPayout + lPayout
            egoCount = egoCount +1

        if iType == 0:
            altPayout = altPayout + payout
            altCount = altCount +1
        else:
            egoPayout = egoPayout + payout
            egoCount = egoCount +1

        if rightiT == 0:
            altPayout = altPayout + rPayout
            altCount = altCount +1
        else:
            egoPayout = egoPayout + rPayout
            egoCount = egoCount +1

        #Calculate average payout of altruist and egoist neighbors and self
        if altCount != 0:
            altFinal = altPayout/altCount
        else:
            altFinal = 0

        if egoCount != 0:
            egoFinal = egoPayout/egoCount
        else:
            egoFinal = 0

        #Assign winner
        if altFinal > egoFinal:
            imitateChoice = 0
        elif egoFinal > altFinal:
            imitateChoice = 1
        else:
            imitateChoice = i.iType

        #Simulate mistakes
        if random() < e:
         	if imitateChoice == 1:
         		imitateChoice = 0
         	else:
         		imitateChoice = 1

        #Create list of winning type for each node
        winnerList.append(imitateChoice)
        pList.append(payout)

        
        #print(leftiT, iType, rightiT, "  AVG alt and ego: ", round(altFinal, 3), round(egoFinal, 3), "  Winner: ", imitateChoice)

        
    
    return winnerList, pList

#Updates generation to be the imitated  
def imitateUpdate(generation, winList, setSize):
    nEgo = 0
    nAlt = 0

    for i in range(len(winList)):
    #print(i, generation.nList[i].iType, winList[i])
        generation.nList[i].setiType(winList[i])

        if(winList[i]) == 0:
            nAlt = nAlt + 1
        else:
            nEgo = nEgo +1

    pAlt = nAlt/setSize
    pEgo = nEgo/setSize
    temp = Info(nAlt,nEgo,pAlt,pEgo)

    for i in range(len(winList)):
        generation.nList[i].setPayout()

    return temp

  
