class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1M = {}
        window = {}

        for ch in s1:
            if ch in s1M:
                s1M[ch] += 1
            else:
                s1M[ch] = 1

        # Window must have exactly len(s1) characters
        size = len(s1)

        if len(s2) < size:
            return False

        # Build the first window
        for r in range(size):
            ch = s2[r]

            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

        if window == s1M:
            return True

        # Slide the window one character at a time
        l = 0

        for r in range(size, len(s2)):
            # Add the new right character
            ch = s2[r]

            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

            # Remove the old left character
            leftChar = s2[l]
            window[leftChar] -= 1

            if window[leftChar] == 0:
                del window[leftChar]

            l += 1

            if window == s1M:
                return True

        return False