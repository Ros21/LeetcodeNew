"""
933. Number of Recent Calls
"""
from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0]<t-3000:
            self.q.popleft()
        return (len(self.q))

        


# Your RecentCounter object will be instantiated and called as such:
recentCounter = RecentCounter()
recentCounter.ping(1)    # requests = [1], range is [-2999,1], return 1
recentCounter.ping(100)  # requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001) # requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002) # requests = [1, 100, 3001, 3002], range is [2,3002], return 3