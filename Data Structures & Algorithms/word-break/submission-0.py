class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp problem 

        dp = [False] * (len(s) + 1)
        dp[0] = True 

        #we now check the each word in wordDict 
        for i in range(len(s)): 
            if not dp[i]: 
                continue 

            for word in wordDict: 
                if s[i:i + len(word)] == word and (i + len(word)) <= len(s):
                    dp[i + len(word)] = True 

        return dp[len(s)] 
