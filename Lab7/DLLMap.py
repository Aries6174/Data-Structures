class Entry:
	# Use the 'Entry' class used in Lab6, since they should be relatively the same
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def setKey(self,key):
		self.key = key

	def getKey(self):
		return self.key

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value

class DLLNode:
	# Use the 'DLLNode' class used in Lab6, since they should be relatively the same
	def __init__(self, entry, nextNode=None, prevNode=None):
		self.entry = entry
		self.nextNode = nextNode
		self.prevNode = prevNode

	def setEntry(self,entry):
		self.entry = entry

	def getEntry(self):
		return self.entry

	def setNext(self,nextNode):
		self.nextNode = nextNode

	def getNext(self):
		return self.nextNode

	def setPrev(self,prevNode):
		self.prevNode = prevNode 

	def getPrev(self):
		return self.prevNode

class DLLMap():
	def __init__(self):
		self.size = 0
		self.headNode = self.tailNode = DLLNode(None)

	def getSize(self):
		# returns the size of the queue
		return self.size

	def isEmpty(self):
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		return self.size == 0

	def find_node(self, key):
		# finds and returns the node with the specified key
		node = self.headNode
		
		while node != None:
			if node.getEntry() != None and node.getEntry().getKey() == key:
				return node
			node = node.getNext()

		return None

	def get(self, key):
		# finds and returns the value of the entry with the specified key
		keyNode = self.find_node(key)

		if keyNode != None:
			return keyNode.getEntry().getValue()
		else: 
			return None



	def put(self, key, value):
		# inserts an entry with the specified key and value in the map; overwrites existing entry if key already exists
		# REQUIRED: Implement 'find_node(key)'
		node = self.find_node(key)

		if node is not None:
			node.getEntry().setValue(value)

		else:
			new_node = DLLNode(Entry(key, value))

			if self.isEmpty():
				self.headNode = new_node
				self.tailNode = new_node
			else:
				self.tailNode.setNext(new_node)
				new_node.setPrev(self.tailNode)
				self.tailNode = new_node

			self.size += 1



	def remove(self, key):
		# removes the entry with the specified key, and returns the entry that was removed
		# REQUIRED: Implement 'find_node(key)'
		node = self.find_node(key)

		if node.getPrev() != None:
			node.getPrev().setNext(node.getNext())
		else:
			self.headNode = node.getNext()

		if node.getNext() != None:
			node.getNext().setPrev(node.getPrev())
		else:
			self.tailNode = node.getPrev()

		self.size -= 1

		remove_entry = node.getEntry()
		node.setNext(None)
		node.setPrev(None)
		return remove_entry
	
		raise Exception("Raise it :|")

	# Iterator Methods
	def keys(self):
		# iterates through the existing entries in the map and prints all the keys in order
		# REQUIRED
		print("\n")
		current = self.headNode
		
		while current is not None:
			if current.getEntry() is not None:
				print(f"Key: {current.getEntry().getKey()}")
			current = current.getNext()

	def values(self):
		# iterates through the existing entries in the map and prints all the values in order
		# REQUIRED
		print("\n")
		current = self.headNode
		
		while current is not None:
			if current.getEntry() is not None:
				print(f"Value: {current.getEntry().getValue()}")
			current = current.getNext()

	def entries(self):
		# iterates through the existing entries in the map and prints all the entries (in the format "key:value") in order
		# REQUIRED
		print("\n")
		current = self.headNode
		
		while current is not None:
			if current.getEntry() is not None:
				print(f"{current.getEntry().getKey()}: {current.getEntry().getValue()}")
			current = current.getNext()
