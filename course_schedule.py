from ast import List

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = { i:[] for i in range(numCourses)}
        for a in prerequisites:
            if a[0] in pre:
                pre[a[0]].append(a[1])
            else: 
                pre[a[0]]= a[1]
        
        visit_set = set()

        def traverse_dfs(course):
            if course in visit_set:
                return False

            if pre[course] == []:
                return True 
                       
            visit_set.add(course)
    
            for pre in pre[course]:
                if not traverse_dfs(pre):
                    return False
            visit_set.remove(course)
            pre[course]= []
            return True
                # if course in pre[key]:
                #     if key in visit_set:
                #         return False
                #     visit_set.add(key)

        
        
        for course in range(0,numCourses):
            if not traverse_dfs(course):
                return False
        
        return True
            

    





        
        


        