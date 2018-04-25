class BinHeap(object):
    def __init__ (self):
        self.heapList=[0]
        self.currentsize=0

    def perUp(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2


    def insert(self,k):
        self.heapList.append(k)
        self.currentsize=self.currentsize+1
        self.perUp(self.currentsize)

    def perDown(self,i):
        while (i*2) <= self.currentsize:
            mc=self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=tmp
            i=mc

    def minChild(self,i):
        if (2*i+1) > self.currentsize:
            return 2*i
        else:
            if self.heapList[i*2] < self.heapList[2*i+1]:
                return 2*i
            else:
                return 2*i+1


    def deleteMin(self):
        retVal=self.heapList[1]
        self.heapList[i]=self.heapList[self.currentsize]
        self.currentsize=self.currentsize-1
        self.heapList.pop()
        self.perDown(1)
        return retVal



    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentsize=len(alist)
        self.heapList=[0]+alist[:]
        while(i>0):
            self.perDown(i)
            i=i-1
