import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra's algorithm
        g = {}

        for start, end, cost in flights:
            if start not in g:
                g[start] = []
            g[start].append((cost, end))

        heap = [(0, src, 0)]  # cost, current airport, flights taken
        best = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops == k + 1:
                continue

            if (node, stops) in best and best[(node, stops)] <= cost:
                continue

            best[(node, stops)] = cost

            # Explore the neighboring airports
            for cost1, nei in g.get(node, []):
                heapq.heappush(heap, (cost + cost1, nei, stops + 1))

        return -1