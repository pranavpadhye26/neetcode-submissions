class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)

        res = []
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
            res.append(node)
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []
        return res[::-1]      