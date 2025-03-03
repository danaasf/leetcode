# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

from ast import List


class Solution:
    def is_number(self,token):
        try:
            int(token)  # Try converting the token to an integer
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_number(token):
                stack.append(int(token))

            else: 
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    res = int(num2) + int(num1)
                elif token == '-':
                    res = num1-num2
                elif token == '*':
                    res = num2 *num1
                else:
                    res = int(num1/num2)
                
                stack.append(res)
        
        return stack.pop()
      
        
        
                

