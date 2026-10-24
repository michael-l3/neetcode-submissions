class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        memo = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(-1)
            memo.append(row)
            
        def dfs(i, j):
            # Base Case 1: If word1 runs out, we must insert all remaining characters of word2
            if i == len(word1):
                return len(word2) - j
                
            # Base Case 2: If word2 runs out, we must delete all remaining characters of word1
            if j == len(word2):
                return len(word1) - i
                
            # Memo check
            if memo[i][j] != -1:
                return memo[i][j]
                
            # If characters match, 0 cost, move both forward
            if word1[i] == word2[j]:
                memo[i][j] = dfs(i + 1, j + 1)
            else:
                # If they don't match, take the minimum of Insert, Delete, and Substitute + 1 cost
                insert_op = dfs(i, j + 1) #inserting the value behind in theory
                delete_op = dfs(i + 1, j) #pretending to delete so we move index forward
                sub_op    = dfs(i + 1, j + 1) #pretend the are the same
                
                memo[i][j] = 1 + min(insert_op, delete_op, sub_op)
                
            return memo[i][j]
            
        return dfs(0, 0)