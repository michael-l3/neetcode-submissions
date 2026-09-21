class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hMap = {}

        for i in range(0,len(numbers)): 
            num = numbers[i]
            compliment = target - num 

            if compliment in hMap: 
                return [hMap[compliment] + 1,i + 1]
            
            hMap[num] = i 
        
