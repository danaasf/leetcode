# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        my_dict = {}
        for a in magazine:
            if a in my_dict:
                val = my_dict[a]
                val +=1
                my_dict[a] = val
            else:
                my_dict[a] = 1
        
        for a in ransomNote:
            if a in my_dict: 
                val = my_dict[a]
                val -=1
                if val == 0:
                    my_dict.pop(a)
                else:
                    my_dict[a]= val
            else:
                return False

        return True 