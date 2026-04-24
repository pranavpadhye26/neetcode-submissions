class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time,tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]
                heap.append((-time, tweetId, uid, index))
            
        heapq.heapify(heap)

        result = []
        while heap and len(result) < 10:
            negtime , tweetId, uid, index = heapq.heappop(heap)
            result.append(tweetId)
        
            if index - 1 >= 0:
                time, nextTweet = self.tweets[uid][index - 1]
                heapq.heappush(heap,(-time , nextTweet, uid, index - 1))
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
