class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        end = len(nums1) - 1
        start1 , start2 = m -1 , n - 1

        while start1 >= 0 and start2 >= 0:
            if nums1[start1] >= nums2[start2]:
                nums1[end] = nums1[start1]
                start1 -= 1
            else:
                nums1[end] = nums2[start2]
                start2 -= 1
            end -= 1
        
        while start2>=0:
            nums1[end] = nums2[start2]
            start2 -= 1
            end -= 1
        