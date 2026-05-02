"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        Dict = {}

        def dfs(node):
            if node in Dict:
                return Dict[node]
            
            var = Node(node.val)
            Dict[node] = var
            for nei_node in node.neighbors:
                var.neighbors.append(dfs(nei_node))
            return var

        return dfs(node) if node else None
        # Dict={}
        
        # def dfs(node):
        #     if node in Dict:
        #         return Dict[node]
            
        #     var=Node(node.val)
        #     Dict[node]=var
        #     for nei_node in node.neighbors:
        #         var.neighbors.append(dfs(nei_node))
        #     return var
        # return dfs(node) if node else None
        
