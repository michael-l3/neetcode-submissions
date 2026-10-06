class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #getting pass this check signals that there is exactly one answer
        if sum(gas) < sum(cost): 
            return -1 

        n = len(gas)
        start = 0 
        tank = 0 

        for i in range(n): 
            tank = tank + gas[i] - cost[i]

            #then we try the next point if it dips below 0
            if tank < 0: 
                start = i + 1 
                tank = 0 
            
        
        return start