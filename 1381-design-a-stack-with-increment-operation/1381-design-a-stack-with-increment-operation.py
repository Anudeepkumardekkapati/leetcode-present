class CustomStack:

    def __init__(self, maxsize: int):
        self.stack=[0]*maxsize
        self.maxsize=maxsize
        self.index=-1
        

    def push(self, x: int) -> None:
        if self.index== self.maxsize-1:
            return
        self.index+=1
        self.stack[self.index]=x
    def pop(self) -> int:
        if self.index==-1:
            return -1
        else:
            val=self.stack[self.index]
            self.index-=1
            return val
    def increment(self, k: int, val: int) -> None:
        limit=min(k,self.index+1)
        for i in range(limit):
            self.stack[i]+=val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)