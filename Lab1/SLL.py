class SLLNode:
	def __init__(self, value, nextNode):
		self.value = value
		self.nextNode = nextNode

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value

	def setNext(self,nextNode):
		self.nextNode = nextNode

	def getNext(self):
		return self.nextNode

class SLL:
	def __init__(self):
		self.first = SLLNode(None,None)					#Sets the value of the first node as None
		self.last = SLLNode(None,None)					#Sets the value of the second node as None
		self.size = 0									#Sets the size as 0

	def isEmpty(self):
		return (self.size == 0)

	def addNode(self,value):
		node_new = SLLNode(value, None)					#Sets the Value but not the nextNode
		if self.size == 0:								#If the Size is Empty
			self.first = node_new						#Setting them both as the first and the last
			self.last = node_new						#Since it is the first Value being inputed
		else:											#If there is an already an existing Node
			self.last.setNext(node_new)					#Setting the last Node into the new node
			self.last = node_new						#Changing the value of the last into the new node
		self.size += 1									#Adding a Node means the Size increases

	def removeNode(self,value):							
		current = self.first							#Records self.first inside current for future use
		previous = None									#Everytime Previous is being used it automatically set it to None, because previous will have a value if used again
		if self.size == 0:								#If the list is empty, removing the Node is pointless
			return

		#Removing the last node from the linked list (if it matches the value)
		if self.first.getValue() == value:				#To determine if the 1st Node's Value matches the Value being pointed out
			self.first = self.first.getNext()			#Move the first reference to the next node
			self.size -= 1								#Lowers the size by 1 since we are removing a Node
			if self.size == 0:							#If the list is not empty
				self.first = SLLNode(None,None)			#Resetting to None
				self.last = SLLNode(None,None)			#Resetting to None
			return
			
		#Removing a node with a specific value in the linked list while maintaining the list
		while current:									#While current has a value
			if current.getValue()==value:				#If the current (node)'s value is equal to the target value
				previous.setNext(current.getNext())		#Updates the next of the previous Node so that it skips the current node
				if current == self.last:				#If the Current Node is the LAST node
					self.last = previous				#Updates the last to the previous node
				self.size -= 1							#Decrementing since we are removing node
				return									#Function Exit
			current = current.getNext()					#Gets the next node in the list