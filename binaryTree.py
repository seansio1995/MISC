class binaryTree(object):
    def __init__(self,root):
        self.key=root
        self.leftChild=None
        self.rightChild=None


    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=binaryTree(newNode)
        else:
            t=binaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t


    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=binaryTree(newNode)
        else:
            t=binaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self,value):
        self.key=value

    def getRootVal(self):
        return self.key


if __name__=="__main__":
    r = binaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())
