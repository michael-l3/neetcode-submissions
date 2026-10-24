"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [] 
        ends = [] 

        for interval in intervals: 
            starts.append(interval.start)
            ends.append(interval.end) 
        
        starts.sort() 
        ends.sort()
        
        #now we go until we finish starts 
        l = 0  #->start pointer
        r = 0  #end->pointer
        minRooms = 0 

        while l < len(starts): 
            #if the starts is less than the first end, then we need a room
            if starts[l] < ends[r]: 
                minRooms += 1 
                l += 1
            else: 
                #that means that a meeting ended and we can reuse the room
                l += 1 
                r += 1 
        
        return minRooms