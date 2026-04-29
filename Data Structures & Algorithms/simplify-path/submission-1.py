class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")
        stack = []
        for ops in pathList:
            if ops == '.' or ops == '':
                continue
            elif ops == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ops)
        return '/' + '/'.join(stack)