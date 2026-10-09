class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = [] 
        cars = []

        for i in range(len(speed)): 
            p = position[i]
            s = speed[i]
            time = (target - p) / s
            cars.append((p,time)) 
        
        cars.sort(reverse=True)

        for p,time in cars: 
            if not stk or time > stk[-1]: 
                stk.append(time)
                
        return len(stk)
        

