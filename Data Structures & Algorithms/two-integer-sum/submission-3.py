class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements={}
        for index,n in enumerate(nums):
            diff=target-n
            if diff in elements:
                return [elements[diff],index]
            elements[n]=index