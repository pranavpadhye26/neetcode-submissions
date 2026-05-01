# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxsoFar):
            if not node:
                return 0
            
            if node.val >= maxsoFar:
                count = 1
            else:
                count = 0
            
            maxsoFar = max(maxsoFar, node.val)
            return count + dfs(node.left,maxsoFar) + dfs(node.right, maxsoFar)
        return dfs(root,root.val)
        # def dfs(node, maxsoFar):
        #     if not node:
        #         return 0
            
        #     if node.val >= maxsoFar:
        #         count = 1
        #     else:
        #         count = 0
            
        #     maxsoFar = max(maxsoFar , node.val)
        #     return count + dfs(node.left,maxsoFar) + dfs(node.right,maxsoFar)
        # return dfs(root,root.val)