
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        g = {}

        for start, end in tickets:
            if start not in g:
                g[start] = []
            g[start].append(end)

        res = []

        def dfs(airport):
            while airport in g and g[airport]:
                nei = g[airport].pop(0)
                dfs(nei)

            res.append(airport)

        dfs("JFK")

        return res[::-1]
