class Solution:
    def findDuplicate(self, nums: List[int]) -> int: 
        seen = {}

        for num in nums:
            if num in seen:
                return num
            seen[num] = seen.get(num, 0) + 1