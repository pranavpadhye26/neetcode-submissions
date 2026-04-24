class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting=defaultdict(list)
        for i in nums:
            if i in counting:
                counting[i]+=1
            else:
                counting[i]=1
        
        sort=sorted(counting.items(),key=lambda x: x[1], reverse=True)

        res=[num for num,freq in sort[:k]]
        return res