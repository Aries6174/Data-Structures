class DLLNode:
	# Insert the 'DLLNode' class you created in Lab1, since they should be the same
	def __init__(self, value):
		self.value = value
		self.nextNode = None
		self.prevNode = None

	def setValue(self,value):
		# REQUIRED
		self.value = value

	def getValue(self):
		# REQUIRED
		return self.value

	def setNext(self,nextNode):
		# REQUIRED
		self.nextNode = nextNode

	def getNext(self):
		# REQUIRED
		return self.nextNode

	def setPrev(self,prevNode):
		# REQUIRED
		self.prevNode = prevNode

	def getPrev(self):
		# REQUIRED
		return self.prevNode

class DLL:
	# Insert the 'DLL' class you created in Lab1, since they should be the same
	def __init__(self):
		self.size = 0
		self.headNode = DLLNode(None)
		self.tailNode = self.headNode
		self.tailNode.setNext(None)
		self.headNode.setPrev(None)

	def getSize(self):
		# returns the size of the queue
		# REQUIRED
		return self.size

	def isEmpty(self):
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		# REQUIRED
		return (self.getSize() == 0)

class DLLDeque(DLL):
	# Note that class "DLLQueue" inherits the class "DLL" attributes and methods

	def first(self):
		# The first() operation returns a reference value to the first element of the deque, but doesn’t remove it
		# REQUIRED
		return self.headNode											#returning the what is set in the headNode but doesnt remove it

	def last(self):
		# The last() operation returns a reference value to the last element of the deque, but doesn’t remove it
		# REQUIRED
		return self.tailNode											#returning the what is set in the tailNode but doesnt remove it

	def insertFirst(self, value):
		# The insertFirst() operation inserts an element at the front of the deque
		# REQUIRED
		insert = DLLNode(value)											#storing the value inside insert	
		insert.setNext(self.headNode)									#setting the next of insert, this will be self.headNode
		insert.setPrev(None)											#setting the previous of insert, this will be set to None since it is the first
		self.headNode.setPrev(insert)									#updating self.headNode and setting its previous as insert
		self.headNode = insert											#we equate headNode to be insert
		self.size += 1													#since we are inserting, we increment

	def insertLast(self, value):
		# The insertLast() operation inserts an element at the end of the deque
		# REQUIRED
		insert = DLLNode(value)											#storing the value inside insert
		insert.setPrev(self.tailNode)									#we set the Previous as the tailNode
		insert.setNext(None)											#we then set the Next to None since it is at the end of the Queue
		self.tailNode.setNext(insert)									#setting the next of the tailNode as Insert
		self.tailNode = insert											#equating the tailNode as Insert
		self.size += 1													#since we are inserting, we increment

	def removeFirst(self):
		# The removeFirst() operation removes the element at the front of the deque
		# This should also return the 'DLLNode' that was removed
		# REQUIRED
		if not self.isEmpty():											#if the Queue is not empty
			first = self.headNode										#we store the headNode in first
			self.headNode = first.getNext()								#we update the next of headNode to become the NEW headNode
			first.setNext(None)											#we cut the connecting of first
			self.size -= 1												#we decrement
			return first												#we return first
		else:
			raise ValueError ("Lmaooooo")
		

	def removeLast(self):
		# The removeLast() operation removes the element at the end of the deque
		# This should also return the 'DLLNode' that was removed
		# REQUIRED
		if not self.isEmpty():											#if the queue is not empty
			last = self.tailNode										#we store the whatever is in the tailNode inside last
			self.tailNode = last.getPrev()								#we update the new tailNode to be the previous of the last
			last.setPrev(None)											#we set the previous of last inside None
			self.size -= 1												#we decrement
			return last													#we return last
		else:
			raise ValueError