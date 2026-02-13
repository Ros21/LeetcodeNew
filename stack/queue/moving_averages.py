"""
346: Moving Average from Data Stream
"""
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        # Initialize your data structure here.
        self.size = size
        self.q = deque()
        
    def next(self, val: int) -> float:
        # Returns the moving average of the last 'size' values of the stream.
        self.q.append(val)
        if len(self.q)>self.size:
            self.q.popleft()
        return round(sum(self.q)/len(self.q),5)


m = MovingAverage(3)
m.next(1)   #  // return 1.0           -> window = [1]
m.next(10)  #  // return 5.5           -> window = [1, 10]
m.next(3)   #  // return 4.66667       -> window = [1, 10, 3]
m.next(5)   #  // return 6.0           -> window = [10, 3, 5]
