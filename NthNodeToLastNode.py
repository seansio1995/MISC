class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None


def NthNodeToLastNode(n, head):
    left_pointer=head
    right_pointer=head

    for i in range(n-1):

        if not right_pointer.nextNode:
            raise LookupError("Error: n is larger than the size of list")

        right_pointer=right_pointer.nextNode

    while  right_pointer.nextNode:
        left_pointer=left_pointer.nextNode
        right_pointer=right_pointer.nextNode
    return left_pointer


def testCase():
    a=Node(1)
    b=Node(2)
    c=Node(3)
    d=Node(4)
    e=Node(5)
    a.nextNode=b
    b.nextNode=c
    c.nextNode=d
    d.nextNode=e

    assert NthNodeToLastNode(3,a)==c
    assert NthNodeToLastNode(4,a)==b
    assert NthNodeToLastNode(5,a)==a
    
if __name__=="__main__":
    testCase()
