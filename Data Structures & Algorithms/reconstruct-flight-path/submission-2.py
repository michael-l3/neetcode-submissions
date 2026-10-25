class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        g = {}

        for start,end in tickets: 
            if start not in g: 
                g[start] = []
            g[start].append(end)
        
        def dfs(airport): 
            #so we are sorting the tickets in lexicographically order
            #then we will pop it off of g *indicating that we are using the ticket 
            while airport in g and g[airport]:
                nei = g[airport].pop(0)
                dfs(nei)
                
            res.append(airport)

        res = [] 
        dfs("JFK")
        return res[::-1]