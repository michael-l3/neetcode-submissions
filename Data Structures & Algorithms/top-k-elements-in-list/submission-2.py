class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create bucket 
        #create counts 
        count = {}

        for number in nums: 
            if number not in count: 
                count[number] = 1 
            else: 
                count[number] += 1 
        #[1,1,2,2,2,3,3,3,3]
        #{1:2,2:3,3:4}

        #create our buckets 
        freq = []
        for _ in range(len(nums)+1): 
            freq.append([])
        
        #freq = [[],[],[],[],[]]
        for number,fre in count.items(): 
            freq[fre].append(number) 
        res = []
        #[[],[],[1],[2],[3]]]
        for i in range(len(freq)-1,-1,-1): 
            for number in freq[i]: 
                res.append(number)

                if len(res) == k: 
                    return res 