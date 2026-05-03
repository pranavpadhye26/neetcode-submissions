from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
        
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            state[node] = 1

            for nei_node in adj[node]:
                if not dfs(nei_node):
                    return False
            
            state[node] = 2
            return True

        for n in range(numCourses):
            if state[n] == 0:
                if not dfs(n):
                    return False
        return True        
        # adj = defaultdict(list)
        # for u,v in prerequisites:
        #     adj[v].append(u)
        
        # state = [0] * numCourses

        # def dfs(node):
        #     if state[node] == 1:
        #         return False
        #     if state[node] == 2:
        #         return True
        #     state[node] = 1

        #     for nei in adj[node]:
        #         if not dfs(nei):
        #             return False
            
        #     state[node] = 2
        #     return True

        # for i in range(numCourses):
        #     if state[i] == 0:
        #         if not dfs(i):
        #             return False
        # return True
