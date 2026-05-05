class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enqueue, process, i) for i , (enqueue,process) in enumerate(tasks)]
        time = 0
        tasks.sort()
        minHeap = []
        res = []
        i = 0
        while i < len(tasks) or minHeap:
            if not minHeap and i < len(tasks) and tasks[i][0] > time:
                time = tasks[i][0]
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1],tasks[i][2]))
                i += 1
            
            process, index = heapq.heappop(minHeap)
            time += process
            res.append(index)
        return res
        
        # tasks = [(enqueue, process, i) for i, (enqueue,process) in enumerate(tasks)]
        # tasks.sort()
        # minHeap = []
        # time = 0
        # res = []
        # i = 0
        # while i < len(tasks) or minHeap:
        #     if not minHeap and i < len(tasks) and tasks[i][0] > time:
        #             time = tasks[i][0]
        #     while i < len(tasks) and tasks[i][0] <= time:
        #         heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
        #         i += 1
            
        #     process, index = heapq.heappop(minHeap)
        #     time += process
        #     res.append(index)
        # return res
        
