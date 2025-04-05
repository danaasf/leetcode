from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        sorted_letters  = sorted(strs)
        final = [''.join(sorted(s)) for s in sorted_letters ]
        strs = sorted(strs)
        my_map = sorted(zip(final,strs))
        
        res = []
        current = [my_map[0][1]]
        print(my_map)
        
        for i in range(1,len(my_map)):
            if my_map[i][0]==my_map[i-1][0]:
                current.append(my_map[i][1])
                continue
            res.append(current)
            current = [my_map[i][1]]

        res.append(current)        
        return res
