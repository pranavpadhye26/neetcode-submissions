class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        state = [0] * numCourses
        res = []
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            state[node] = 1

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            res.append(node)
            state[node] = 2
            return True
        
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []
        return res[::-1]

