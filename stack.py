class stack:
    def __init__(self):
        self.items=[]


    def isEmpty(self):
        return self.items==[]


    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


    def peek(self):
        return self.items[len(self.items)-1]


    def size(self):
        return len(self.items)


if __name__=="__main__":
    mystack=stack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    print(mystack.size())
    print(mystack.peek())
    print(mystack.pop())
    print(mystack.size())
