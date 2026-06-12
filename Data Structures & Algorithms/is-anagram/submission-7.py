class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = Counter(s)
        countT = Counter(t)

        if countS == countT:
            return True
        else:
            return False