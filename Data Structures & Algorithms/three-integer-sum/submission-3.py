class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # nums.sort()
        # for i,no in enumerate(nums):
        #     if i>0 and no==nums[i-1]:
        #         continue
        
        #     l,r=i+1,len(nums)-1
        #     while l<r:
        #         threeSum=no+nums[l]+nums[r]
        #         if threeSum<0:
        #             l+=1
        #         elif threeSum>0:
        #             r-=1
        #         else:
        #             res.append([no,nums[l],nums[r]])
        #             l+=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        # return res

        res = []
        nums.sort()

        for i in range(0,len(nums)):
            if nums[i] > 0: break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res