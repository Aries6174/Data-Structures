class DLLNode:
	def __init__(self, value, nextNode, prevNode):
		self.value = value
		self.nextNode = nextNode
		self.prevNode = prevNode

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value

	def setNext(self,nextNode):
		self.nextNode = nextNode

	def getNext(self):
		return self.nextNode

	def setPrev(self,prevNode):
		self.prevNode = prevNode

	def getPrev(self):
		return self.prevNode

class DLL:
	def __init__(self):
		self.size = 0											#keeps track of the number of codes
		self.first = DLLNode(None,None,None)					#This will represent the first node
		self.last = DLLNode(None,None,None)						#This will represent the last node

	def isEmpty(self):											
		return (self.size == 0)									#returns true if size is 0 and false otherwise

	def addNode(self, value):									
		new_node = DLLNode(value, None, None)					#Object created will give a value, whiile nextMode and prevMode is none because it doesnt have any next or previous nodes
		if self.size == 0:										#If the list is Empty
			self.first = new_node								#The Node being added is Now Both the First
			self.last = new_node								#and the Last Node
		else:													#If the List is not empty
			self.last.setNext(new_node)							#Updating last nextNode of the last node to point it to the new_node
			new_node.setPrev(self.last)							#same thing but this time sets the new_node is being ponted to the current last node.
			self.last = new_node								#this makes the new node as the last of the list
		self.size += 1											#Since we are adding node, we add one to the list

	def removeNode(self, value):
		if self.size == 0:										#if the list is empty
			return												#There is no point of removing something

		if self.size == 1:										#If there is a SINGLE Node that exist in the list
			if self.first.getValue() == value:					#If the value of the first is equal to the current Value
				self.first = DLLNode(None,None,None)			#This replaces first with a new DLL Node with None Attributes
				self.last = DLLNode(None,None,None)				#This replaces last with a new DLL Node with None attributes
				self.size -= 1									#Decrements size, since we are removing a Node in an existing list
				return											#Function end

		if self.first.getValue() == value:						#If the value is the same with the value fo the first Node(but if there are more than 1 node in the list)
			original = self.first								#Original is a reference to the first node, which will be removed in this if statement
			self.first = original.getNext()						#whatever is next to the original will be put inside self.first, it also removes the reference to the first node
			#
			original.setNext(DLLNode(None,None,None))			#Severs the connection of the removed Node
			original.setPrev(DLLNode(None,None,None))			
			self.first.setPrev(DLLNode(None,None,None))			
			#
			self.size -= 1										#Decrementing since we are removing an existing Node
			return		

		#If the value doesnt match the First Node AND there are more than one node on the list
		currentNode = self.first								#Initializing current node as the first one
		while currentNode.getNext() is not None:				#Loop that iterates throught the list until it reaches the final node
			if currentNode.getNext().getValue() == value:		#Checks if the value of the next node is the same as the target value, if it does. the next node needs to be removed.
				removedNode = currentNode.getNext()				#Creates a reference to the node that is being removed
				currentNode.setNext(removedNode.getNext())		#Updates the nextNode reference so that we can remove the removed node from the list
				if removedNode.getNext():						#Ensures that the connections betweem the adjacent nodes are updated after removing the node being removed
					removedNode.getNext().setPrev(currentNode)	

				removedNode.setNext(None)						#Clears the references in the removed node to make sure it is isolated from the list
				removedNode.setPrev(None)						

				self.size -= 1									#Decrements the list
				if currentNode.getNext() is None:				#Checks if the currentNode is the Last Node.
					self.last = currentNode						#If it does it updates itself as the last one.
					return										
			currentNode = currentNode.getNext()					#This assigns the next node to become the current Node. This allows you to taverse the whole list.