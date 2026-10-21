
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        g = {}

        for a, b in edges:
            if a not in g:
                g[a] = []
            if b not in g:
                g[b] = []

            g[a].append(b)
            g[b].append(a)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        state = [UNVISITED] * n

        def dfs(node, parent):
            if state[node] == VISITING:
                return False

            if state[node] == VISITED:
                return True

            state[node] = VISITING

            for nei in g.get(node, []):
                if nei == parent:
                    continue

                if state[nei] == VISITING:
                    return False

                if not dfs(nei, node):
                    return False

            state[node] = VISITED
            return True

        if not dfs(0, -1):
            return False

        for i in range(n):
            if state[i] == UNVISITED:
                return False

        return True
