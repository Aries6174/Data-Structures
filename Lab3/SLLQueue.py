class SLLNode:
	# Insert the 'SLLNode' class you created in Lab2, since they should be the same
	def __init__(self, value):
		self.value = value
		self.nextNode = None

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

class SLL:
	# Insert the 'SLL' class you created in Lab2, since they should be the same
	def __init__(self):
		self.size = 0
		self.frontNode = SLLNode(None)
		self.frontNode.setNext(SLLNode(None))

	def getSize(self):
		# returns the size of the queue
		# REQUIRED
		return self.size

	def isEmpty(self):
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		# REQUIRED
		return (self.size == 0)

class SLLQueue(SLL):
	# Note that class "SLLQueue" inherits the class "SLL" attributes and methods

	def front(self):
		# The front() operation returns a reference value to the front element of the queue, but doesn’t remove it
		# REQUIRED
		if self.size == 0:
			return SLLNode(None)
		else:
			return self.frontNode

	def enqueue(self, value):
		# The enqueue() operation inserts an element at the end of the queue
		# If the capacity is full, you are not allowed to enqueue() an element to the queue
		# REQUIRED
		node_new = SLLNode(value)
		
		if not self.isEmpty():
			current = self.frontNode
			while current.getNext() is not None:
				current = current.getNext()

			current.setNext(node_new)
		else:
			self.frontNode = node_new

		self.size += 1

	def dequeue(self):
		# The dequeue() operation removes the element at the front of the queue
		# This should also return the 'Element' that was removed
		# REQUIRED
		if self.isEmpty():
			raise Exception ("Empty lmao")
		else:
			removed = self.frontNode
			self.frontNode.setNext(None)
			self.frontNode = self.frontNode.getNext()
			self.size -= 1
			return removed