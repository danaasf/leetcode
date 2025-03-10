# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dig_to_letter = {
            1: "" , 2: ["a","b","c"] , 3: ["d","e","f"], 4:["g","h","i"], 5:["j","k","l"],
            6: ["m","n","o"], 7: ["p","q","r","s"], 8:["t","u","v"], 9: ["w","x","y","z"]
        }
        res = []
        size = len(digits)

        if digits == "":
            return []

        def combinations (digits,cur,i):

            if i == size:
                res.append(cur)
                return 

            for c in self.dig_to_letter[int(digits[i])]:
                combinations(digits,cur+c ,i+1)

        combinations(digits,"",0)
        return res


            

            





        