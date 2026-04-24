class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x : x[0])
        res.append(intervals[0])
        for start,end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(end,res[-1][1])
            else:
                res.append([start,end])
        return res
        
