class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)

        for num , freq in count.items():
            if freq > len(nums) // 3:
                res.append(num)
        return res
        