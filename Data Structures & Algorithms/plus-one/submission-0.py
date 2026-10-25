class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [] 
        currDigit = ""

        for i in range(len(digits)): 
            number = digits[i]
            currDigit += str(number)
        
        currDigit = str(int(currDigit) + 1)

        for i in range(len(currDigit)): 
            res.append(int(currDigit[i]))
        return res