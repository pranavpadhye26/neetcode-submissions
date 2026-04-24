class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

        # res = ""
        # for s in strs:
        #     res += str(len(s))+"#"+s
        # return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            count = int(s[i:j])
            word = s[j + 1: j + 1 + count]
            res.append(word)
        
            i = j + 1 + count
        return res






        # res = []
        # i = 0
        # while i < len(s):
        #     j = i
        #     while s[j] != '#':
        #         j += 1
        #     l = int(s[i:j])
        #     word = s[j+1:j+1+l]
        #     res.append(word)

        #     i = j+1+l
        # return res
            