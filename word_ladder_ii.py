from collections import defaultdict, deque
import collections
from typing import List
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:        
        wordSet = set(wordList)
        wordSet.discard(beginWord)
        adj1 = collections.defaultdict(list)
        adj2 = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + ch + word[i+1:]
                    if tmp in wordSet and tmp!=word:
                        adj1[word].append(tmp)
                        adj2[tmp].append(word)
        
        
        queue = deque([])
        if not beginWord in wordList:
            for i in range(len(beginWord)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = beginWord[:i] + ch + beginWord[i+1:]
                    if tmp in wordSet and tmp!=beginWord:
                        adj1[beginWord].append(tmp)
                        adj2[tmp].append(beginWord)

        queue.append(beginWord)
        res = []
        depth_map = collections.defaultdict(int)
        depth_map[beginWord]=1

        while queue:
            
            node = queue.popleft()
            steps = depth_map[node]

            if node == endWord:
                break

            for nei in adj1[node]:
                if nei in wordSet and nei != node:
                    queue.append(nei)
                    wordSet.discard(nei)
                    depth_map[nei]= steps+1


        def dfs(node,path):

            if node==beginWord:
                res.append(path[::-1])
                return 
            
            steps=depth_map[node]
            for nei in adj2[node]:
                if nei in depth_map and depth_map[nei] == steps-1 :
                    dfs(nei,path+[nei])
            
        if endWord in depth_map:
            dfs(endWord,[endWord])
        
        return res




        
                





        # my_map = collections.defaultdict(list)
        # my_dict = collections.defaultdict(list)
        # for word in wordList:
        #     for i in range(len(word)):
        #         tmp = word[:i] + "*" + word[i+1:]
        #         my_map[tmp].append(word)
        #         my_dict[word].append(tmp)
        
        # adj = collections.defaultdict(list)
        # for word in wordList:
        #     for pattern in my_dict[word]:
        #         for option in my_map[pattern]:
        #             adj[word].append(option)

        # queue = deque([])
        # if not beginWord in wordList:
        #     for i in range(len(beginWord)):
        #             node =  beginWord[:i] + "*" + beginWord[i+1:]
        #             for w in my_map[node]:
        #                 if not w == beginWord:
        #                     adj[beginWord].append(w)

        # queue.append((beginWord,[beginWord]))
        # res = []
        # visited= set()
        # found = False
        
        # while queue and not found:
        #     level_size = len(queue)
        #     level_visited = set()

        #     for _ in range(level_size):
        #         popped = queue.popleft()
        #         node = popped[0]
        #         path= popped[1]
                

        #         if node == endWord:
        #             res.append(path[:])
        #             found = True 
        #             continue

        #         for nei in adj[node]:
        #             if not nei in visited:
        #                 queue.append((nei,path+[nei]))
        #                 level_visited.add(nei)

        #     visited.update(level_visited)

        # return res




        
                