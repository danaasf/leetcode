
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.adjacency = defaultdict()
        for edge in times:
            if not edge[0] in self.adjacency:
                self.adjacency[edge[0]]= [edge[1:]]
            else:
                self.adjacency[edge[0]].append(edge[1:])

        self.heap = []
        heapq.heapify(self.heap)
        heapq.heappush(self.heap,(0,k))
        visited = set()
        res = 0

        while self.heap:
            source= heapq.heappop(self.heap)
            if source[1] not in visited:
                visited.add(source[1])
            else:
                continue
            time= source[0]
            res = max(res,time)
            if source[1] not in self.adjacency:
                continue
            for edge in self.adjacency[source[1]]:
                if edge[0] not in visited:
                    heapq.heappush(self.heap,(time+edge[1],edge[0]))

            
        if len(visited)==n:
            return res
        else:
            return -1
                
            

            
            


      







        