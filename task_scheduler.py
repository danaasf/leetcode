# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.


from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int: 
        hashmap = {}
        for a in tasks:
            if a in hashmap: 
                hashmap[a] = hashmap.get(a) + 1
            else: 
                hashmap[a] = 1
        
        res = 0
        size = len(hashmap)
        most_frq = 0
        for entry in hashmap: 
            if hashmap[entry] > most_frq: 
                most_frq = hashmap[entry]
        count = 0
        for a in hashmap:
            if hashmap[a] == most_frq:
                count +=1 
        
        interval = n + 1
        repeat = most_frq - 1
        res = interval * repeat + count
        
        
        return max(len(tasks),res)
