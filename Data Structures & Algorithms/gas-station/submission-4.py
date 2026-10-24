class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Rule 1: If total gas is less than total cost, complete circuit is impossible
        if sum(gas) < sum(cost):
            return -1
            
        current_tank = 0
        start_station = 0
        
        for i in range(len(gas)):
            # Accumulate the net gas at this station (gas gained - cost to leave)
            current_tank += gas[i] - cost[i]
            
            # If the tank goes negative, we can't start from our current `start_station`
            if current_tank < 0:
                # Reset the start to the next station
                start_station = i + 1
                # Reset the tank for the new journey
                current_tank = 0
                
        return start_station