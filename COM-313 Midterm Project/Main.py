#Griffin McAlinden

from Individual import Node
from Generation import Generation
from Info import *
from random import *
from Imitation import *


#NOTE: buttons can bring up text boxes so the user can edit the intial values?
def main():
    c = .49
    ave = .5
    setSize = 20
    e = 0
    history = []
    historyP = []
    nodes = []
    rounds = 5
    info = []
    
    

    #Generate Linked list for nodes as well as agen list for imitation
    gen1 = Generation()
    agen2 = []



    #NOTE: eventually implement if else so the player can choose random or specific
    #Create list of nodes of size 'setSize' with a weighted random choice between egoist and altruist
    for i in range(setSize):
        #For each node generate a random number between 0 and 1.
         #If its above or equal to ave the node becomes an egoist
        if random() >= ave:
            rand = 1
        else:
            rand = 0
        nodes.append(Node(rand,c))


    #NOTE: possible logic for specific selection
    #-user enters size of set then selects manual
    #   for i in range(setSize):
    #       -user selects iType of node
    #       nodes.append(Node(iType,c))
    #
    #-After the Nodes are selected user is given the option to remove a node by entering its location in the list
    #   gen1.remNodePos(position)
    #
    #-After Nodes are selected the user is given the option to add an extra node onto the end
    #   gen1.addEnd(node)
    #
    #-After the Nodes are selected the user is given the option to insert a node into the middle 
    # REMEMBER TO REMIND THE USER WHERE THE NODE WILL END UP
    #   gen1.addNodePos(node, position)
    #



    #used for testing
    """for i in range(setSize):
        nodes.append(Node(1,c))

    for i in range(3):
        nodes[i].setiType(0)"""



    #Add first node to list
    gen1.addStart(nodes[0])
    #Add the rest of the nodes to the list
    for i in range(1, setSize):
        gen1.addEnd(nodes[i])
 
    #Create a nested array that simulates a matrix in order to store the history of the generations. 
    #(NOTE: Use values from arrays to show the last 1 or 2 generations?)
    temp = []
    temp2 = []
    nEgo = 0
    nAlt = 0
    for i in range(len(gen1.nList)):
        temp.append(gen1.nList[i].iType)
        temp2.append(gen1.nList[i].payout)

    
        if gen1.nList[i].iType == 0:
            nAlt = nAlt+1
        else:
            nEgo = nEgo + 1
    pAlt = nAlt/setSize
    pEgo = nEgo/setSize
    info.append(Info(nAlt,nEgo,pAlt,pEgo))
            
    history.append(temp) 
    historyP.append(temp2)

    #Simulates 'rounds' number of rounds of imitations. 
    for i in range(rounds):
        winList, pList= imitation(gen1, e)
        history.append(winList)
        
        tempInfo = imitateUpdate(gen1, winList, setSize)
        historyP.append(pList)
        info.append(tempInfo)

    #Used for testing to print each simulated round
    for i in range(len(history)):
        print(history[i], end = "  ")
        #print(historyP[i], end = "  ")
        info[i].infoTest()
    
main()
