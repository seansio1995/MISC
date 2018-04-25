class maxStack(object):
    def __init__(self):
        self.stack=Stack()
        self.maxStack=Stack()


    def push(self,num):
        self.stack.push(num)

        if self.maxStack.peek() is None or self.maxStack.peek() <= num:
            self.maxStack.push(num)


    def pop(self):
        num=self.stack.pop()

        if num==self.maxStack.peek():
            self.maxStack.pop()
        return num


    def
