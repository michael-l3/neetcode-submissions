class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        cur = {}

        for ch in s1:
            if ch not in s1Map:
                s1Map[ch] = 1
            else:
                s1Map[ch] += 1

        have = 0
        need = len(s1Map)

        l = 0

        for r in range(len(s2)):
            ch = s2[r]

            if ch not in s1Map:
                cur = {}
                have = 0
                l = r + 1
                continue

            if ch not in cur:
                cur[ch] = 1
            else:
                cur[ch] += 1

            if cur[ch] == s1Map[ch]:
                have += 1

            while cur[ch] > s1Map[ch]:
                leftChar = s2[l]
                cur[leftChar] -= 1

                if cur[leftChar] < s1Map[leftChar]:
                    have -= 1

                l += 1

            if have == need:
                return True

        return False