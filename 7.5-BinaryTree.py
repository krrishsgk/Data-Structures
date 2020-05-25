class binaryTree:

    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newObj):
        if self.leftChild == None:
            self.leftChild = binaryTree(newObj)

        else:
            t = binaryTree(newObj)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newObj):
        if self.rightChild == None:
            self.rightChild = binaryTree(newObj)

        else:
            t = binaryTree(rightObj)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
    return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
