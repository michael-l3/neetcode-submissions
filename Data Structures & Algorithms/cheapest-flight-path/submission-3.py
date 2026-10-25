class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = {}

        for start, end, cost in flights:
            if start not in g:
                g[start] = []
            g[start].append((end, cost))

        # (total cost, current airport, flights taken)
        minHeap = [(0, src, 0)]
        best = {}

        while minHeap:
            cost, start, flights_taken = heapq.heappop(minHeap)

            if start == dst:
                return cost

            if flights_taken == k + 1:
                continue

            if (start, flights_taken) in best and best[(start, flights_taken)] <= cost:
                continue

            best[(start, flights_taken)] = cost

            for nei, nei_cost in g.get(start, []):
                heapq.heappush(minHeap, (cost + nei_cost, nei, flights_taken + 1))

        return -1