class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value 

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key
    
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
    
class DLLNode:
    def __init__(self, entry, nextNode=None, prevNode=None):
        self.entry = entry
        self.nextNode = nextNode
        self.prevNode = prevNode
        
    def setEntry(self, value):
        self.entry.setValue(value)

    def getEntry(self):
        return self.entry

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

    def setPrev(self, prevNode):
        self.prevNode = prevNode

    def getPrev(self):
        return self.prevNode

class UnsortedPQ:
    def __init__(self):
        self.headNode = DLLNode(None)
        self.tailNode = DLLNode(None)
        self.size = 0
    
    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def find_min(self):
        if not self.isEmpty():
            minNode = self.headNode
            currentNode = self.headNode
            while currentNode.getNext() is not None:
                if currentNode.entry.key < minNode.entry.key:
                    minNode = currentNode
                currentNode = currentNode.getNext()
            return minNode
        else:
            raise Exception("Empty PQ")
        
        
    def insert(self, entry):
        newNode = DLLNode(entry)
        if self.isEmpty():
            self.tailNode = newNode
            self.headNode = newNode
        else:
            newNode.setPrev(self.tailNode)
            self.tailNode.setNext(newNode)
            self.tailNode = newNode
        self.size += 1

    def remove_min(self):
        if self.isEmpty():
            print("Nothing to remove Lmao")
            return None
        else:
            minNode = self.find_min()    
            if self.size == 1:
                self.tailNode = None
                self.headNode = None
            elif minNode == self.tailNode:
                self.tailNode = minNode.getPrev()
            elif minNode == self.headNode:
                self.headNode = minNode.getNext()
            else:
                minNode.getPrev().setNext(minNode.getNext())
                minNode.getNext().setPrev(minNode.getPrev())
            self.size -= 1
            return minNode.getEntry()

    def min(self):
        return self.find_min().getEntry()

class SortedPQ:
    def __init__(self):
        self.size = 0
        self.headNode = self.tailNode = DLLNode(None)
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def insert(self, entry):
        new_node = DLLNode(entry)
        if self.isEmpty():
            self.headNode = new_node
            self.tailNode = new_node
        else:
            current_node = self.headNode
            while current_node is not None and current_node.getEntry().key < entry.key:
                current_node = current_node.getNext()
            
            # Insert the new node
            if current_node is None:
                # Insert at the end
                new_node.setPrev(self.tailNode)
                self.tailNode.setNext(new_node)
                self.tailNode = new_node
            elif current_node == self.headNode:
                # Insert at the beginning
                new_node.setNext(self.headNode)
                self.headNode.setPrev(new_node)
                self.headNode = new_node
            else:
                # Insert in the middle
                new_node.setPrev(current_node.getPrev())
                new_node.setNext(current_node)
                current_node.getPrev().setNext(new_node)
                current_node.setPrev(new_node)
        
        self.size += 1
        
    def remove_min(self):
        if self.isEmpty():
            print("Nothing to remove Lmao")
            return None
        else:
            min_node = self.headNode
            if self.size == 1:
                # Case: Only one element in the SortedPQ
                self.headNode = None
                self.tailNode = None
            else:
                # Case: Remove the first (minimum) element
                self.headNode = min_node.getNext()
                self.headNode.setPrev(None)

            self.size -= 1
            return min_node.getEntry()
    
    def min(self):
        return self.headNode.getEntry()
