class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): 
            return False 
        
        # 1. Size the memo board with + 1 to handle out-of-bounds index states
        memo = [] 
        for r in range(len(s1) + 1): 
            row = [] 
            for c in range(len(s2) + 1): 
                row.append(-1)
            memo.append(row)
        
        def dp(index1, index2): 
            # 2. Base case: If both strings are fully used up, we successfully interleaved!
            if index1 == len(s1) and index2 == len(s2): 
                return True 
            
            # 3. Memo check (Safe to do because indices are bounded within + 1 size)
            if memo[index1][index2] != -1: 
                return memo[index1][index2]
            
            # 4. Try matching with s1 if it's not exhausted and matches s3
            match_s1 = False
            if index1 < len(s1) and s1[index1] == s3[index1 + index2]:
                match_s1 = dp(index1 + 1, index2)
                
            # 5. Try matching with s2 if it's not exhausted and matches s3
            match_s2 = False
            if index2 < len(s2) and s2[index2] == s3[index1 + index2]:
                match_s2 = dp(index1, index2 + 1)
            
            # 6. Save result in the board and return
            memo[index1][index2] = match_s1 or match_s2
            return memo[index1][index2]
        
        return dp(0, 0)