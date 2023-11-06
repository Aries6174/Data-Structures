class Element:
	def __init__(self, value, index):
		self.value = value
		self.index = index

	def setValue(self, value):
		self.value = value

	def getValue(self):
		return self.value
	
class Array:
	def __init__(self):
		self.contents = []					#The Array
		self.size = 0						#Empty Set has 0 size

	def isEmpty(self):
		return (self.size == 0)

	def addElement(self, value):
		element = Element(value, self.size)	#Calling the element class
		self.contents.append(element)		#Append the element inside the contents
		self.size += 1						#Adding 1 to the size

	def removeElement(self, index):				
		if 0 <= index < self.size:			#if the index is not negative or above the current size of the array
			self.contents.pop(index)		#removes the value that is inside that index
			self.size -= 1					#lowers the size by 1