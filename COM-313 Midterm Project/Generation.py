#TO BE UPDATED/CLEANED UP. I need to consolidate some of the code as I believe some parts are unnecesary


#Griffin McAlinden

#The class 'Generation' creates a linked list of nodes that represents a generation of individuals
 #start: a pointer to the first node in the linked list
 #end: a pointer to the last node in the linked list
 #length: the number of nodes in the list
 #nList: an array that contains the nodes allowing for easy access to the middle of the list

#Methods:
 #main methods
  #addStart(self, node): MUST BE USED FOR FIRST NODE IN GENERATION. Sets 'start' and 'end pointers to 
   #'node', set the node's position to 0, and append node to 'nList'
  #addEnd(self, node): Adds a node to the linked list and appends itself to the array. Set itself as
   #the new 'end' then update the neighbor pointers of the old end, itself, and start. Updates the payouts
   #of itself, the old end, and start
  #remNodePos(self, position): Removes the 'position'nth node, update its neighors' pointer and payouts, and
   #reduces the 'position' of all following nodes by 1
  #addNodePos(self, node, position): Inserts 'node' into the list after 'position'nth node in the list.
   #If position == 1 the node will be inserted after the node in position 1 in the array such that it is
   #the third node in the list.
   
 #Can be used to fix issues
  #setStart(self, start): set pointer representing the first node to 'start' 
  #setEnd(self, end): set pointer representing the first node to 'end'
  #setLength(self, length): set int representing length to 'length'



from Individual import Node


class Generation:
    def __init__(self, start =0, end =0, length =0, nList = []):
        self.start = 0
        self.end = 0
        self.length = 0
        self.nList = nList

    #Set the first node in the list
    def setStart(self, start):
        self.start = start
    #Set the last node in the list
    def setEnd(self, end):
        self.end = end
    #Set the length of the list
    def setLength(self, length):
        self.length = length

    #Called once for the first node in the generation
    def addStart(self, node):
        self.start = node
        self.end = node
        node.setPos(0)
        self.nList.append(node)

    #Add a node to the end of the list, update neighbors, and length
    def addEnd(self, node):
        #update length
        self.length = self.length + 1
        #Fix for when node is second item in list
        if self.length == 1:
            self.end.setLeft(node)
        #Update right neighbor of old end, left neighbor of new end
        self.end.setRight(node)
        node.setLeft(self.end)
        node.setPos(self.length)
        #Set new payout of old end
        self.end.setPayout()
        #update end pointer to the new node
        self.end = node
        self.nList.append(node)
        #Update right neighbor of new node, left neighbor of start
        node.setRight(self.start)
        self.start.setLeft(node)
        #Update payout of start and the new node
        node.setPayout()
        self.start.setPayout()

    #Remove a node based on its position then reduce the position of all following nodes by 1
    def remNodePos(self, position):
        #found tracks if the node has been found
        found = 0
        temp = self.start
        #If position == to the starting node
        if position == 0:
            #Update neighbors
            self.end.setRight(temp.right)
            temp.right.setLeft(self.end)
            temp.left.setPayout()
            temp.setPayout()
            temp.right.setPayout()
            #Reduce pos by 1 for each node in list
            for i in range(self.length):
                temp = temp.right
                temp.setPos(temp.pos -1)
            #Clear old start's attributes
            temp = self.start
            temp.setLeft(None)
            temp.setRight(None)
            temp.setPos(None)
            self.nList.remove(temp)
            self.start = self.end.right
        else:
            #Iterate through list to find node with pos == to position
            for i in range(self.length+1):
                if (temp.pos == position):
                    #Make left and right neighbors of the node neighbors
                    temp.left.setRight(temp.right)
                    temp.right.setLeft(temp.left)
                    temp.left.setPayout()
                    temp.setPayout()
                    temp.right.setPayout()
                    #Clear pointers from node
                    temp2 = temp.left
                    temp.setLeft(None)
                    temp.setRight(None)
                    temp.setPos(None)
                    self.nList.remove(temp)

                    found = 1
                #For all nodes after the found node: reduce pos by 1
                if found == 1:
                    temp2 = temp2.right
                    temp2.pos = temp2.pos -1
                else:
                    temp = temp.right
            self.start.setPos(0)
        self.length = self.length -1

    #DO NOT USE FOR END OR START NODE.
    #Add node into list after the position ie: position =1 will result in the node
     #being placed into position 2, or the 3rd node in the list.
    def addNodePos(self, node, position):
        #Declare variables temp and found. Found tracks if the position has been reached
        temp = self.start
        found = 0
        #Iterate through the list until position is reached
        for i in range(self.length+1):
            #When position is reached insert node and update neighbors
            if temp.pos == position:
                node.setRight(temp.right)
                node.setLeft(temp)
                temp.setRight(node)
                node.right.setLeft(node)
                node.left.setPayout()
                node.setPayout()
                node.right.setPayout()
                node.setPos(position+1)
                found = 1
                self.nList.insert(position+1, node)
                temp = node
            #Move temp to the right neighbor and, if the new node has been inserted, increment pos by 1
            temp = temp.right
            if found == 1:
                temp.setPos(temp.pos + 1)
        #Fix start position and increment length by 1
        self.start.setPos(0)
        self.length = self.length + 1

 