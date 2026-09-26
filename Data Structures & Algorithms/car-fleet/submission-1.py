class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = [] 
        tracker = []
        #will need to keep track of time and when it gets there 
        #the len of the stk will be the answer because we will only append 
        #if the time is > the last stk time 

        for i in range(len(position)): 
            time = (target - position[i]) / speed[i]
            tracker.append((position[i],time))

        tracker.sort(reverse=True)

        for pos,time in tracker: 
            if not stk or time > stk[-1]: 
                stk.append(time)
        
        return len(stk)
        
