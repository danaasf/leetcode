from typing import List

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False
    
    def addWord(self,word):
        current = self
        for c in word: 
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.leaf = True
         

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        Trie = TrieNode()
        for word in words:
            Trie.addWord(word)
        res = set()
        visit = set()

        def dfs(i,j,node,temp):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or (i,j) in visit or board[i][j] not in node.children:
                return 

            visit.add((i,j))
            temp+=board[i][j]
            node = node.children[board[i][j]]
            if node.leaf: 
                res.add(temp)
             
            
            dfs(i+1,j,node,temp)
            dfs(i-1,j,node,temp) 
            dfs(i,j+1,node,temp) 
            dfs(i,j-1,node,temp)
            visit.remove((i,j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                    dfs(i, j, Trie, "")
        
        return list(res)


         
        