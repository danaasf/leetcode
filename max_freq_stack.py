class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq_map = {}
        self.count_map = {}
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.freq_map[val] = self.freq_map.get(val,0) + 1

        if self.freq_map[val] > self.max_freq:
            self.max_freq = self.freq_map.get(val)

        if self.freq_map[val] in self.count_map: 
            self.count_map[self.freq_map[val]].append(val)
        else:
            self.count_map[self.freq_map[val]]= [val]
    
        
    def pop(self) -> int:
        if len(self.count_map[self.max_freq]) > 1 :
            res = self.count_map[self.max_freq].pop()
            self.freq_map[res] = max(0,self.freq_map[res]-1) 

        else: 
            res = self.count_map.pop(self.max_freq)[0]
            self.freq_map[res] = max(0,self.freq_map[res]-1) 
            self.max_freq = max(0,self.max_freq-1)

        return res


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()