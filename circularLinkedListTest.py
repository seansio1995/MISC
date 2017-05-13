class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None



def cycle_check(Node):
    marker1=Node
    marker2=Node

    while marker1.nextNode!=None and marker2.nextNode!=None:
        marker1=marker1.nextNode
        marker2=marker2.nextNode.nextNode


        if marker1==marker2:
            return True
    return False

def testCase():
    a=Node(1)
    b=Node(2)
    c=Node(3)
    a.nextNode=b
    b.nextNode=c

    x=Node(1)
    y=Node(2)
    z=Node(3)
    x.nextNode=y
    y.nextNode=z
    z.nextNode=x

    assert cycle_check(a)==False
    assert cycle_check(x)==True

if __name__=="__main__":
    testCase()
