class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0

        left , right = 0 , len(heights) - 1

        while left < right:
            vol = min(heights[left],heights[right]) * (right - left)
            maxVol = max(maxVol,vol)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return maxVol
            
