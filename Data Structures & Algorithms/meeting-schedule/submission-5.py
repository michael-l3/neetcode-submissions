class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        # Sort intervals by their start time
        intervals.sort(key=lambda x: x.start) 
        
        currInterval = intervals[0]

        for interval in intervals[1:]: 
            # If the next meeting starts BEFORE the current meeting ends, there's an overlap!
            if interval.start < currInterval.end: 
                return False 
            else: 
                currInterval = interval 

        return True