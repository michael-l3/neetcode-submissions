from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        d = {}

        for number in hand:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1

        while d:
            minVal = min(d)

            for number in range(minVal, minVal + groupSize):

                if number not in d:
                    return False

                d[number] -= 1

                if d[number] == 0:
                    del d[number]

        return True