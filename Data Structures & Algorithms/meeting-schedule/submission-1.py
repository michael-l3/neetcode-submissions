"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: 
            return True
            
        intervals.sort(key=lambda interval: interval.start) 
        previous = intervals[0]

        for i in range(1,len(intervals)): 
            if previous.end <= intervals[i].start: 
                previous = intervals[i]
            else: 
                return False 
        
        return True