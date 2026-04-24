class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1 = Counter(s1)
        countWindow = Counter(s2[:len(s1)])

        if countWindow == countS1: return True
        for right in range(len(s1),len(s2)):
            countWindow[s2[right]] += 1
            countWindow[s2[right - len(s1)]] -= 1
            if countWindow[s2[right - len(s1)]] == 0:
                del countWindow[s2[right - len(s1)]]
            if countWindow == countS1:
                return True
        return False
        

