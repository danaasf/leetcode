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
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)