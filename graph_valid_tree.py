# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:

# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

# Output:
# true

from collections import defaultdict
import collections
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #if root - connected to two nodes at most
        #if mid node - connected to three nodes at most
        #if leaf - connected to one 
        adj = collections.defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = collections.defaultdict(int)
        def dfs(node,parent):
            if node in visited:
                return False 
            visited[node]= visited[node]+1
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False

            return True
        if dfs(0,-1):
            if len(visited) < n :
                return False
            for key,val in visited.items(): 
                if val>3:
                        return False
            
            return True
        return False
            

        