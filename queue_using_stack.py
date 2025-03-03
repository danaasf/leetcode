class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []
        

    def push(self, x: int) -> None:
        while(self.first): 
            temp = self.first.pop()
            self.second.append(temp)
        
        self.first.append(x)
        while(self.second):
            temp= self.second.pop()
            self.first.append(temp)

    def pop(self) -> int:
        return self.first.pop()
        

    def peek(self) -> int:
        first_in = self.first.pop()
        self.first.append(first_in)
        return first_in



    def empty(self) -> bool:
        if self.first:
            return False
        else: 
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()