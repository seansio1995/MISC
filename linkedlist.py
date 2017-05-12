
##Single LinkedList
class LinkedListNode(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None


a=LinkedListNode(1)
b=LinkedListNode(2)
c=LinkedListNode(3)

a.nextNode=b
b.nextNode=c


#Double Linkedlist

class DoubleLinkedListNode(object):
    def __init__(self,value):
        self.value=value
        self.prevNode=None
        self.nextNode=None

a=DoubleLinkedListNode(1)
b=DoubleLinkedListNode(2)
c=DoubleLinkedListNode(3)

a.nextNode=b
b.prevNode=a

b.nextNode=c
c.prevNode=b
