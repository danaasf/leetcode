# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

class Trie:

    def __init__(self):
        self.adjacency = {}
        

    def insert(self, word: str) -> None:
        current = self.adjacency
        for l in range(0,len(word)):
            if word[l] not in current: 
                current[word[l]]={}
            current = current[word[l]]
            
        current['*']= True
           
        print(current)
       
    def search(self, word: str) -> bool:
        
        current_dict = self.adjacency
        i = 0 
        while i<len(word):
            if word[i] not in current_dict:
                return False
            current_dict= current_dict[word[i]]
            i+=1
        
        if '*' in current_dict:
            return True 
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
      
        current_dict = self.adjacency
        i = 0 
        while   i<len(prefix):
            if prefix[i] not in current_dict:
                return False
            current_dict= current_dict[prefix[i]]
            i+=1

        return True
        

# class TrieNode: 
#     def __init__(self):
#         self.val = ""
#         self.children = {} 
#         self.end= False
        
# class PrefixTree:

#     def __init__(self):
#         self.words = [None]*26
        
#     def insert(self, word: str) -> None:
#         if self.words[ord(word[0])- ord('a')]:
#             root = self.words[ord(word[0])- ord('a')]
#         else:
#             root = TrieNode()
#         root.val = word[0]
#         current = root
#         for c in word[1:]:
#             if c not in current.children:
#                 current.children[c] = TrieNode()
#             current = current.children[c]
#         current.end = True
#         self.words[ord(word[0])- ord('a')]= root

#     def search(self, word: str) -> bool:
#         if not self.words[ord(word[0])-ord('a')] :
#             return False
#         root = self.words[ord(word[0])-ord('a')]
#         for c in word[1:]:
#             if c not in root.children: 
#                 return False
#             root = root.children[c]
#         if root.end:
#             return True
#         return False

        
#     def startsWith(self, prefix: str) -> bool:
#         if not self.words[ord(prefix[0])-ord('a')] :
#             return False
#         root = self.words[ord(prefix[0])-ord('a')]
#         for c in prefix[1:]:
#             if c not in root.children: 
#                 return False
#             root = root.children[c]
        
#         return True

        
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

