class BINARYTREE:
    def __init__(self, item):
        self.item = item                            #Setting item
        self.parent = None                          #Parent
        self.left = None                            #The Left
        self.right = None                           #The Right

    def getElement(self):               
        return self.item                            #return The item

    def setLeft(self, node):
        self.left = node                            #setting the left

    def setRight(self, node):
        self.right = node                           #setting the right

    def getLeft(self):
        return self.left                            #getting the left

    def getRight(self):
        return self.right                           #getting the right

    def setParent(self, node):                      
        self.parent = node                          #setting the Parent

    def getParent(self):
        return self.parent                          #getting the parent

class LinkedListTree:
    def __init__(self):                             
        self.rootNode = None                        #Setting The rootNode to None

    def getRoot(self):
        return self.rootNode                        #returning the rootNode

    def setRoot(self, itemNode):
        if type(itemNode).__name__ == 'BINARYTREE': #Check if the type of itemNode is BINARYTREE
            self.rootNode = itemNode                #setting rootNode to the itemNode
        else:
            self.rootNode = BINARYTREE(itemNode)    #create a new instance of BINARYTREE with itemNode and set self.rootNode to it

    def setLeft(self, parentIndex, value):          #setting Left
        newNode = BINARYTREE(value)             #Initiating BinaryTree inside newnode
        if parentIndex.getLeft() is None:           #if The left of parentIndex is empty
            newNode.setParent(parentIndex)          #set the new parent of newNode to be the new Parent
            parentIndex.setLeft(newNode)            #set the left of the parentIndex to be the newNode
        else:
            rightChild = parentIndex.getLeft().getRight()   #Initating the right child
            leftChild = parentIndex.getLeft().getLeft()     #Initiating the left child
            newNode.setParent(parentIndex)          #The Parent of the newNode will be the inputted ParentIndex
            if rightChild is not None:              #if there is a rightChild
                newNode.setRight(rightChild)        #set the right of the new Node to be the rightChild
                rightChild.setParent(newNode)       #set the parent of the right Child to be the newNode
            if leftChild is not None:               #if there is a leftChild
                newNode.setLeft(leftChild)          #set the left of the newNode to be the leftChild
                leftChild.setParent(newNode)        #setting the parent of the left Child to be the newNode
            parentIndex.setLeft(newNode)            #The Left of the parent Index will be the new Node since we have adjusted everything

    def setRight(self, parentIndex, value):         #setting the Right
        newNode = BINARYTREE(value)                 #initiating Binarytree inside newNode
        if parentIndex.getRight() is None:          #if the right of the parent exist
            newNode.setParent(parentIndex)          #setting the parent of newNode as the ParentIndex
            parentIndex.setRight(newNode)           #setting the right of the ParentIndex as newNode
        else:         
            rightChild = parentIndex.getRight().getRight()  #inititaing the right right child of the parent index inside right childe
            leftChild = parentIndex.getRight().getLeft()    #initiating the left Childe
            newNode.setParent(parentIndex)          #setting the Parent of newNode as The parentIndex
            if rightChild is not None:              #if the rightChild exist
                newNode.setRight(rightChild)        #setting the Right of newNode to be the rightChild
                rightChild.setParent(newNode)       #setting the parent of the Right CHilde to be new Node
            if leftChild is not None:               #if there is a left Childe
                newNode.setLeft(leftChild)          #setting the Left of New Node to be the Left Child
                leftChild.setParent(newNode)        #setting the parent of the left Childe to be the new Node
            parentIndex.setRight(newNode)           #setting the RIght of the parenIndex to be newNode

    def inorder(self, node):                        #for inorder
        result = []                                 #create Array result
        if node is not None:                        #if node exist
            result += self.inorder(node.getLeft())  #kapoy na ako comments ;-;
            result.append(node.getElement())
            result += self.inorder(node.getRight())
        return result

    def preorder(self, node):     
        result = []
        if node is not None:
            result.append(node.getElement())
            result += self.preorder(node.getLeft())
            result += self.preorder(node.getRight())
        return result

    def postorder(self, node):
        result = []
        if node is not None:
            result += self.postorder(node.getLeft())
            result += self.postorder(node.getRight())
            result.append(node.getElement())
        return result

def create_linked_BT():

        binary = LinkedListTree()

        binary.setRoot('A')                                                 #Create root_node and first level of tree.
        binary.setLeft(binary.getRoot(), 'B')
        binary.setRight(binary.getRoot(), 'C')
        
        binary.setLeft(binary.getRoot().getLeft(), 'D')                     #Create second level of tree.
        binary.setRight(binary.getRoot().getLeft(), 'E')

        binary.setLeft(binary.getRoot().getRight(), 'F')
        binary.setRight(binary.getRoot().getRight(), 'G')

        binary.setLeft(binary.getRoot().getLeft().getRight(), 'H')          #Create third level of tree. 
        binary.setRight(binary.getRoot().getLeft().getRight(), 'I')

        binary.setLeft(binary.getRoot().getRight().getLeft(), 'J')
        binary.setRight(binary.getRoot().getRight().getLeft(), 'K')
        

        return binary

binary_tree = create_linked_BT()

print("""
Linked List Tree:
""")

# Inorder traversal
inorder_result = binary_tree.inorder(binary_tree.getRoot())
print("Inorder traversal:", inorder_result)

# Preorder traversal
preorder_result = binary_tree.preorder(binary_tree.getRoot())
print("Preorder traversal:", preorder_result)

# Postorder traversal
postorder_result = binary_tree.postorder(binary_tree.getRoot())
print("Postorder traversal:", postorder_result)
