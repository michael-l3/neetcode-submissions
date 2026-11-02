
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        word = strs[0]

        for i in range(len(word)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or word[i] != strs[j][i]:
                    return res

            res += word[i]

        return res
