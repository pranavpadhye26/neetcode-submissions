class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        need = len(countT)
        have = 0
        left = 0
        window = {}
        resLen = float("inf")
        resLeft, resRight = 0 , 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = (right - left + 1)
                    resLeft = left
                    resRight = right
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        return s[resLeft:resRight + 1] if resLen != float("inf") else ""

        