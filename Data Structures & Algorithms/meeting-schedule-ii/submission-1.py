"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: 
            return 0

        starts = [] 
        ends = []

        for interval in intervals: 
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()
        
        room = 0 
        endPointer = 0

        for start in starts: 
            if start >= ends[endPointer]: 
                room -= 1
                endPointer += 1
             
            room += 1 
        
        return room
