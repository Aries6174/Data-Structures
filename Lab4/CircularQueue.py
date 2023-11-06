class Element:
	# Insert the 'Element' class you created in Lab1, since they should be the same
	def __init__(self, value, index = 0):
		self.value = value
		self.index = index

	def setValue(self,value):
		# REQUIRED
		self.value = value

	def getValue(self):
		# REQUIRED
		return self.value
	
	def getIndex(self):
		# REQUIRED
		return self.index

class Array:
	def __init__(self, capacity=10):
		self.size = 0 				# The 'size' attribute must not exceed the 'capacity'		
		self.capacity = capacity
		self.contents = [None]*self.capacity
		self.DEFAULT_EXPANSION = 5
		self.frontIndex = 0
		self.rearIndex = 0
		
	def getSize(self):
		# returns the size of the queue
		# Note that the size is based on frontIndex and rearIndex
		# REQUIRED
		return self.size

	def getCapacity(self):
		# returns the capacity of the queue
		# REQUIRED
		return self.capacity

	def isEmpty(self):
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		# REQUIRED
		return (self.size == 0)

	def expand(self):
		# The expand() operation increases the capacity when necessary
		self.capacity += self.DEFAULT_EXPANSION
		self.contents += ([None]*self.DEFAULT_EXPANSION)

	def wrapAround(self):
		# The wrapAround() operation resets the Array back where head is at index 0
		# Note: You will only use this function when capacity is full and you wish to enqueue()
		# REQUIRED
		fixContents = [None] * self.capacity												#fixContents will has the length of self.capacity since it represents the maximum number of elements allowed
		for i in range(self.capacity):														#The loop will run based on what the capacity is
			self.contents[i] = self.contents[(self.frontIndex + i) % self.capacity]			#for every i, this uses a modular arithmetic, where everytime self.frontIndex + i is exceeding the bounds, it wraps around to the beginning
		self.contents = fixContents															#assigning fix contents to self.contents, which it updates the contents
		self.frontIndex = None																#The front index into None, which is common when representing the front index in a circular array
		self.rearIndex = self.size - 1														#setting the rear index is set to be self.size subtracted to 1

class CircularQueue(Array):
	# Note that class "CircularQueue" inherits the class "Array" attributes and methods

	def front(self):
		# The front() operation returns a reference value to the front element of the queue, but doesn’t remove it
		# REQUIRED
		if self.isEmpty():																	#if the Array is empty, this returns an Element with None
			return Element(None)
		else:																				#Otherwise, this returns the first value of the array
			return self.contents[self.frontIndex]

	def enqueue(self, value):
		if self.size >= self.capacity:
			self.expand()
			self.wrapAround()
		newEl = Element(value, self.rearIndex)
		self.contents[self.rearIndex] = newEl
		self.rearIndex = (self.rearIndex + 1) % self.capacity
		self.size += 1							#In Enqueue, we increment

	def dequeue(self):
		# The dequeue() operation removes the element at the front of the queue
		# This should also return the 'Element' that was removed
		# REQUIRED
		if self.isEmpty():																	#If Empty we raise exception
			raise Exception ("Wala unod XD")
		else:
			removed = self.contents[self.frontIndex]										#storing the first element inside removed
			self.frontIndex = (self.frontIndex + 1) % self.capacity							#self.frontIndex updates the front index to be the next one in the queue
			self.size -= 1																	#In Dequeue we decrement
			return removed																	#we then return the first element that was removed