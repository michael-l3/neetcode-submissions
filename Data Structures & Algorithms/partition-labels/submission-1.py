class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = [] 

        #so we are trying to figure out where it doesnt repeat anymore 
        #easiest way is to keep track of the last place of where that letter is for each character 
        d = {}
        for i,ch in enumerate(s): 
            d[ch] = i
        
        # {'x': 3, 'y': 4, 'z': 7, 'b': 9, 'i': 10, 's': 11, 'l': 12}
        #now just keep track of currEnd
        currEnd = 0 
        startIndex = 0
        for i in range(len(s)): 
            ch = s[i]
            currEnd = max(d[ch],currEnd)

            if i == currEnd: 
                res.append(currEnd - startIndex + 1)
                startIndex = currEnd + 1
                currEnd = currEnd + 1 
            
        return res
        
    