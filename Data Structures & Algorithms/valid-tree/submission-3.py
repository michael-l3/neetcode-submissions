
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        g = {}

        for a, b in edges:
            if a in g:
                g[a].append(b)
            else:
                g[a] = [b]

            if b in g:
                g[b].append(a)
            else:
                g[b] = [a]

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for nei in g.get(node, []):
                if nei == parent:
                    continue

                if nei in visited:
                    return False

                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
