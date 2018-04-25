class HashTable(object):
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size


    def put(self,key,data):
        hashvalue=self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nextslot=self.rehash(hashvalue,len(self.slots))

                while self.slots[nextslot] is not None and self.slots[nextslot]!=key:
                    nextslot=self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot]=data
    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size


    def get(self,key):
        startslot=self.hashfunction(key,len(self.slots))
        data=None
        stop=False
        found=False
        pos=startslot
        while  self.slots[pos]!=None and not stop and not found:
            if self.slots[pos]==key:
                found=True
                data=self.data[pos]
            else:
                pos=self.rehash(pos,len(self.slots))
                if pos==startslot:
                    stop=True
        return data



    def __getitem__(self,key):
        return self.get(key)


    def __setitem__(self,key,data):
        self.put(key,data)



h = HashTable(6)
h[0]="Zero"
h[1]="One"
h[2]="Two"
h[3]="Three"
h[4]="Four"
h[8]="Eight"
print(h.slots)
print(h.data)
