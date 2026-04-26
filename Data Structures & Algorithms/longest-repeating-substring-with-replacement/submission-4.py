class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left , maxLen , maxFreq = 0 , 0 , 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFreq = max(maxFreq , count[s[right]])
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, (right - left + 1))
        return maxLen