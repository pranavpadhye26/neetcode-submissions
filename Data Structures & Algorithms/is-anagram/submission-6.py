class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr1 = Counter(s)
        arr2 = Counter(t)

        return (arr1 == arr2)