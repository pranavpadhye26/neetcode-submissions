class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counting_dict={}
        for i in nums:
            if i in counting_dict:
                counting_dict[i]+=1
            else:
                counting_dict[i]=1
        
        duplicates=any(count>1 for count in counting_dict.values())
        if duplicates:
            return True
        else:
            return False