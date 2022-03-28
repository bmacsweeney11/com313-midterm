#Griffin McAlinden

#The class 'Node' create a node that contains a variety of important information.
 #iType: either 0 or 1. if iType == 0 then the individual is an altruist and if iType == 1 then it is an egoist
 #cost: An altruist's payout is reduced by cost
 #generation : NOT USED ANYMORE. TO BE DELETED IF USE NOT FOUND BY DUE DATE
 #right: pointer to the nodes "right" neighbor
 #left: pointer to the nodes "left" neighbor
 #payout: the payout of the individual. The method setPayout() must be called for it to update to its neighbors
 #benefit: the value an altruist provides its neighbors
 #position: represents the node's place in its generation

#Methods:
 #setGen(self, generation): replaces generation
 #setiType(self, iType): changes the iType of the node. 0 for altruist and 1 for egoist
 #setRight(self, pointer): sets the pointer representing the right neighbor to 'pointer'
 #setLeft(self, pointer): sets the pointer representing the left neighbor to 'pointer'
 #setPos(self, position): changes the int representing the node's location in the list to 'position'
 #setPayout(self): updates the value of 'payout' with its current neighbors

class Node:
	def __init__(self, iType, cost, generation = 0, right=0, left=0, payout=0, benefit = 1, position = None):
		self.generation = generation
		self.iType= iType
		self.right = right
		self.left = left
		self.payout=payout
		self.cost = cost
		self.benefit = benefit
		self.pos = position
	#Set generation of the node
	def setGen(self, generation):
		self.generation = generation
	#set the class of the node, 0=altruist and 1=egoist
	def setiType(self, iType):
		   self.iType=int(iType)

	#set the pointer representing the right neighbor 
	def setRight(self, pointer):
		    self.right = pointer

	#Set the pointer representing the left neighbor
	def setLeft(self, pointer):
		   self.left = pointer

	#Set the position of the node in array that makes up its generation
	def setPos(self, position):
		self.pos = position

	#find and assign the payout, calculate by getting the classes of the neighbors
	def setPayout(self):
		self.payout = 0
		ben = self.benefit
		#get and assign the values of the left and right neighbors’ classes
		rCharacter = self.right.iType
		lCharacter = self.left.iType
			 
		#if the node is an altruist subtract cost from the total payout
		if self.iType == 0:
			self.payout = self.payout-self.cost

		#calculate the node’s payout
		if rCharacter == 0:
		    self.payout = self.payout + ben
		if lCharacter == 0:
		    self.payout = self.payout + ben