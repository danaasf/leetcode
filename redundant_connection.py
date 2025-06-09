
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.


from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # adj = collections.defaultdict(list)
        # for edge in edges: 
        #     adj[edge[0]].append(edge[1])
        #     adj[edge[1]].append(edge[0])

        # res = []
        # def dfs(node,parent,current):

        #     if current and node in current:
        #         res.extend(current[current.index(node):])
        #         return

        #     neighbors = adj[node]

        #     for i,nei in enumerate(neighbors):  
        #         if nei == parent:
        #             continue 
        #         if dfs(nei,node,current+[node]):
        #             break
        #     return res
        
        # root , size = 0,0
        # for i in adj :
        #     if len(adj[i])>size:
        #         root=i
        #         size= len(adj[i])

        
        # nodes = dfs(root,0,[])
        # for [x,y] in edges[::-1]:
        #     if x in nodes and y in nodes:
        #         return [x,y]

        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n1):
            if par[n1] == n1:
                return par[n1]
            
            par[n1] = find(par[n1])
            return par[n1]

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return False
            
            if rank[p1]>=rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True

        for [x,y] in edges: 
            if not union(x,y):
                return [x,y]
            

            



            
        
            

            

            


        
        