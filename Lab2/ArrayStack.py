class Element:
	def __init__(self, value, index):
		self.value = value
		self.index = index

	def setValue(self,value):
		self.value = value								#setting value to be itself

	def getValue(self):
		return self.value								#returning the value of itself

	def getIndex(self):
		return self.index								#returning the index of itself

class Array:
	def __init__(self, capacity=10):			
		self.contents = []
		self.size = 0 	
		self.capacity = capacity
		self.DEFAULT_EXPANSION = 5

	def getCapacity(self):
		return self.capacity							#returning the capacity 

	def isEmpty(self):
		return self.size == 0							#boolean wether or not it is true or false

	def expand(self):
		self.capacity += self.DEFAULT_EXPANSION			

class ArrayStack(Array):
	def top(self):
		if not self.isEmpty():								#if self.size is above 0 since 0 is empty and it the bottom limit
			return self.contents[self.size - 1]				#returns the top value(size is subtracted to 1 cause size started from 0)
		else:												#otherwise if it is below 0 or its empty
			return None										#return None since it is empty

	def push(self, value):									
		if self.size != self.capacity:						#If size has not yet reach the capacity
			element = Element(value, self.size)				#initialize Element with its value and index inside element
			self.contents += [element]						#add that element inside the contents
			self.size += 1									#Increment size since we are pushing
		else:
			raise Exception("FULL STACK")					#Exception raise

	def pop(self):
		if not self.isEmpty():								#if the the size is not empty
			elemtop = self.contents[self.size - 1]			#store what the top element is inside a variable
			self.contents[self.size - 1] = None
			self.size -= 1									#Decrements Size
			return elemtop									#returning the element that is at the top
		else:
			raise Exception("NOTHING TO POP LMAO")			#Exception raise	