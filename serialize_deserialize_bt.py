# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return "[]"
        queue = deque([root])
        data = []
    
        
        while queue:
            popped = queue.popleft()
            if popped:
                data.append(str(popped.val))

                queue.append(popped.left)
                queue.append(popped.right)
                
            else: 
                data.append("null")

        
        return "[" + ",".join(data) + "]"
            


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data== "[]":
            return None 
        
        data = data[1:-1].split(',')
        root = TreeNode(int(data[0]))
        queue = deque([root])

        index = 1 
        while queue and index < len(data)  :
            popped = queue.popleft()
            if data[index] != "null":
                popped.left = TreeNode(int(data[index]))
                queue.append(popped.left)
            index+=1

            if data[index] != "null":
                popped.right = TreeNode(int(data[index]))
                queue.append(popped.right)
            
            index+=1
        
        return root


        # def deserializeT (n):
        #     if n >= len(data) or if data[n] is None :
        #         return None 

        #     root.val = data[n]            
        #     left = deserializeT(n+1)
        #     right = deseralizeT(n+2)

        #     root.left = left
        #     root.right = right
        
        # root= deserializeT(0)

         

        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))