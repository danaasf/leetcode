from collections import Counter, deque
import string
from typing import List


# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        
        wordList = set(wordList)
        visited = set()
        visited.add(beginWord)
        queue = deque([(beginWord,1)])


        while queue:
            popped , path= queue.popleft()
            if popped == endWord:
                return path

            for i in range(0,len(popped)):
                for letter in list(string.ascii_lowercase):
                    mod = popped[:i] + letter + popped[i+1:]

                    if mod in wordList and not mod in visited :
                        queue.append((mod, path+1))
                        visited.add(mod)

        return 0  

                

 
        



        