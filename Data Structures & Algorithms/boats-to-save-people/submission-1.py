class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        left , right = 0 , len(people) - 1
        while left <= right:
            total = people[left] + people[right]
            if total <= limit:
                res += 1
                left += 1
                right -= 1
            elif total > limit:
                res += 1
                right -= 1
        return res