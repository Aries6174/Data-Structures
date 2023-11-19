class Array:
    def __init__(self, capacity):
        self.capacity = capacity                            #setting the capacity of the Array
        self.items = [None] * capacity                      #Multiplying it from the number of items that currently exist

    def getElement(self, index):                            #getting the element
        if 0 <= index < self.capacity:                      #if the index is between 0 and self.capcity
            return self.items[index]                        #return that specific index
        raise IndexError(" Osmanthus wine taste the same as I remember, ")   # But where are those who share the memory

    def setElement(self, index, item):                      #setting the element at that specidix index
        if 0 <= index < self.capacity:                      #if the index is between self.capacity and 0
            self.items[index] = item                        #setting the item in that specific index
        else:
            raise IndexError(" Oratrice Machanique d'Analyse Cardinale, ")   #The Judgement of the ..


class ArrayTree:    
    def __init__(self, capacity=50):                        #setting up the Array
        self.array = Array(capacity)                        #Initiating Array with the capacity

    def setRoot(self, item):                                #setting the Root
        index = self.getRoot()                              #we use getRoot which is just 1
        self.array.setElement(index, item)                  #setting the element of the array with the index and item

    def setLeft(self, parentIndex, value):                   #setting the Left of the index
        index = self.getLeftIndex(parentIndex)              #we get the index of what is at the left of the parent
        self.array.setElement(index, value)                  #we then set that element inside the array

    def setRight(self, parentIndex, value):                  #setting the Left if the index
        index = self.getRightIndex(parentIndex)             #we get the index of what is at the left of the parent
        self.array.setElement(index, value)                  #we then set that element inside the array

    def getRoot(self):                                      #return the first node
        return 1                                            #The root is always the first Node

    def getLeftIndex(self, index):                          #return the what is at the LeftIndex
        return index * 2                                    #The Left of the Parent is always even, multiplying it by 2 will return the node index

    def getRightIndex(self, index):                         #return what is at the RightIndex
        return (index * 2) + 1                              #The right of the Parent is always odd, multiplying by 2 and adding by 1 will return the node index

    def inorder(self, index, result):                           #Inorder
        if self.array.getElement(index) is not None:            #will keep running till none are left
            self.inorder(self.getLeftIndex(index), result)      #we get the index of left aswell as the result
            result.append(self.array.getElement(index))         #we then append that element of the index inside result
            self.inorder(self.getRightIndex(index), result)     #now we get the right index

    def preorder(self, index, result):                          #Preorder
        if self.array.getElement(index) is not None:            #Will keep running till none are left
            result.append(self.array.getElement(index))         #storing the element first inside result
            self.preorder(self.getLeftIndex(index), result)     #Moves to the Left
            self.preorder(self.getRightIndex(index), result)    #Moves to the Right

    def postorder(self, index, result):
        if self.array.getElement(index) is not None:            
            self.postorder(self.getLeftIndex(index), result)    #Traverse to the Left
            self.postorder(self.getRightIndex(index), result)   #Traverse to the Right
            result.append(self.array.getElement(index))         #append to the Result


def MakeArrayTree():
    binary = ArrayTree()                                        #calling Arraytree


#Setting everything manuallly, sry if ganto
    binary.setRoot('3') #Root

    binary.setLeft(binary.getRoot(), '87')  #Node 2
    binary.setRight(binary.getRoot(), '20') #Node 3

    binary.setLeft(binary.getLeftIndex(binary.getRoot()), '53') #Node 4
    binary.setRight(binary.getLeftIndex(binary.getRoot()), '241')   #Node 5

    binary.setLeft(binary.getRightIndex(binary.getRoot()), '123')   #Node 6
    binary.setRight(binary.getRightIndex(binary.getRoot()), '5275') #Node 7

    binary.setLeft(binary.getRightIndex(binary.getLeftIndex(binary.getRoot())), '237') #Node 8
    binary.setRight(binary.getRightIndex(binary.getLeftIndex(binary.getRoot())), '453') #Node 9

    binary.setLeft(binary.getLeftIndex(binary.getRightIndex(binary.getRoot())), '297') #Node 10
    binary.setRight(binary.getLeftIndex(binary.getRightIndex(binary.getRoot())), '168') #Node 11

    return binary


#SAMPLE

print("""
Array Tree:
""")

#Inorder Example
result = []
binary = MakeArrayTree()
print("Inorder traversal:", end=' ')
binary.inorder(binary.getRoot(), result)
print(result)

#Preorder Example
result = []
binary = MakeArrayTree()
print("Preorder traversal:", end=' ')
binary.preorder(binary.getRoot(), result)
print(result)

#Postorder Example
result = []
binary = MakeArrayTree()
print("Postorder traversal:", end=' ')
binary.postorder(binary.getRoot(), result)
print(result)

