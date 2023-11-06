class SLLNode:
	def __init__(self, value):
		self.value = value
		self.nextNode = None

	def setValue(self,value):
		self.value = value							#Setting up the value

	def getValue(self):
		return self.value							#returning the value
	
	def setNext(self,nextNode):
		self.nextNode = nextNode					#Setting up the nextNode

	def getNext(self):
		return self.nextNode 

class SLL:
	def __init__(self):
		self.size = 0
		self.topNode = SLLNode(None)
		self.topNode.setNext(SLLNode(None))

	def isEmpty(self):
		return self.size == 0						#Boolean whether or not the size is Empty or not

class SLLStack(SLL):
	def top(self):	
		if not self.isEmpty():						#if the size is not empty
			return self.topNode						#we return the topNode
		else:
			return SLLNode(None)					#we return Nothing since it is empty

	def push(self, value):
		node_new = SLLNode(value)					#Initialize node_new with SLLNode containing a value

		if not self.isEmpty():						#if it is not empty
			node_new.setNext(self.topNode)			#setting the newnode's next node to be the top node
			self.topNode = node_new					#the new topNode is now the new node

		else:
			self.topNode = node_new					#if it is empty let the new node be the topNode automatically
		
		self.size += 1								#increments size

	def pop(self):
		if not self.isEmpty():						#if it isnt empty
			removed = self.topNode					#the topNode will be stored in removed
			self.topNode = self.topNode.getNext()	#the new top node will now be the next in the stack since it goes left to right
			removed.setNext(SLLNode(None))			#Clearing what is the next variable for removed
			self.size -= 1							#Decrementing Size since we are poppin
			return removed							#return the topNode
		else:
			raise Exception("EMPTY STACK")