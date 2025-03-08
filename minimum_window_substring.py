from collections import Counter

class Solution:
    def min_windowWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
            
        chars_of_t= Counter(t)
        min_window = (-1,-1)
        length = float("infinity")
        need = len(chars_of_t)
        have = 0 
        start = 0  
        window = {}
        
        for r in range(len(s)):
            end = s[r]
            window[end]= window.get(end,0) + 1

            if end in chars_of_t and window[end] == chars_of_t[end]:
                have += 1
            
            while have == need: 
                if r - start + 1 < length:
                    length = r - start + 1
                    min_window = (start, r)
                
                window[s[start]] -=1
                if s[start] in chars_of_t and window[s[start]]<chars_of_t[s[start]]:
                    have -=1
                start +=1
            
        if  length != float("infinity"):
            return s[min_window[0]:min_window[1]+1]
            
        else:
            return ""
                





sol = Solution()
print(sol.min_windowWindow("ADOBECODEBANC","ABCA"))
                     

            

            

        