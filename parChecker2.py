class Stack:
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


def parCheck(SymbolString):
    s=Stack()
    index=0
    balanced=True
    while index < len(SymbolString) and balanced:
        symbol=SymbolString[index]
        if symbol in "({[":
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced=False
            else:
                top=s.pop()
                if not match(top,symbol):
                    balanced=False
        index+=1
    if s.isEmpty() and balanced:
        return True
    else:
        return False



def match(open,close):
    opens="({["
    closes=")}]"
    return opens.index(open)==closes.index(close)



print(parCheck('{{([][])}()}'))
print(parCheck('[{()]'))
