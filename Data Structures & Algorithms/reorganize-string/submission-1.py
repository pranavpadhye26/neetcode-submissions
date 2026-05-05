class Solution:
    def reorganizeString(self, s: str) -> str:
        # freq = Counter(s)
        # heap = []
        # res = ""
        # for ch,count in freq.items():
        #     heapq.heappush(heap, (-count,ch))
        
        # prev = None
        # while heap:
        #     count , ch = heapq.heappop(heap)
        #     res = res + ch
            
        #     if prev:
        #         heapq.heappush(heap,prev)
        #     prev = (count + 1, ch) if count + 1 < 0 else None

        # return res if len(res) == len(s) else ""

        heap = []
        freq = Counter(s)
        res = ""
        for ch, count in freq.items():
            heapq.heappush(heap,(-count,ch))
        
        prev = None
        while heap:
            count , ch = heapq.heappop(heap)
            res += ch

            if prev:
                heapq.heappush(heap,prev)
            prev = (count + 1, ch) if count + 1 < 0 else None
        return res if len(res) == len(s) else ""