class Dequeue:
    def __init__(self):
        self.items=[]


    def isEmpty(self):
        return self.items==[]


    def addfront(self,item):
        self.items.append(item)

    def addrear(self,item):
        self.items.insert(0,item)

    def removefront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__=="__main__":
    d=Dequeue()
    d.addfront(1)
    d.addrear(2)
    d.addrear(3)
    d.addfront(100)
    print(d.removefront())
    print(d.size())
