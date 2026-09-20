class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #something to keep its position and time it takes to get there
        cars = [] 

        for i in range(len(position)): 
            time = (target - position[i]) / speed[i]   #--> how long it takes to get there 
            cars.append((position[i],time))
        
        cars.sort(reverse=True) #-> now we are closes to the target instead  

        stk = []
        #now we iterate through the cars and create a stk to keep track of how many fleets 
        for pos, time in cars: 
            if not stk or time > stk[-1]: 
                stk.append(time)
        
        return len(stk)