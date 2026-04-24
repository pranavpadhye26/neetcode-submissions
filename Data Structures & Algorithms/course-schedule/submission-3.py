from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d=defaultdict(list)
        for u,v in prerequisites:
            d[v].append(u)
        print(d)
        
        indeg=[0]*numCourses

        for i in range(numCourses):
            for ele in d[i]:
                indeg[ele]+=1
        
        q=deque()
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        
        while q:
            element=q[0]
            q.popleft()
            for e in d[element]:
                indeg[e]-=1
                if indeg[e]==0:
                    q.append(e)

        for count in indeg:
            if count>0:
                return False
        return True
