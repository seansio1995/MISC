# 1   2  3 4
#Now the current pointer is at 2
#current next point to 3 now
#in order to reverse it we let current points to 1
#The pointer then moves to 1 forward
# 2 1 3 4 Now the current is 3
#2 3 1 4
#2 3 4 1


class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None



def reverse(head):
    current=head
    previous=None
    nextNode=None

    while current:
        nextNode=current.nextNode
        current.nextNode=previous


        #move 1 node forward
        previous=current
        current=nextNode

    return previous


a=Node(1)
b=Node(2)
c=Node(3)

a.nextNode=b
b.nextNode=c


print(a.nextNode.value)
print(b.nextNode.value)
#print(c.value)

reverse(a)

print(c.nextNode.value)
print(b.nextNode.value)
#print(c.value)
