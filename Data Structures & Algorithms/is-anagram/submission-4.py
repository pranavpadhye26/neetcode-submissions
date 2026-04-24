class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dec = {}
        for ch in s:
            if ch in dec:
                dec[ch] += 1
            else:
                dec[ch] = 1
        
        for ch in t:
            if ch not in dec or dec[ch] <= 0:
                return False
            dec[ch] -= 1
        
        return True
                