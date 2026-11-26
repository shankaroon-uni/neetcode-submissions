class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        nodes = {i: [] for i in range(n)}

        for par, node in edges:
            nodes[node].append(par)
            nodes[par].append(node)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for n in nodes[node]:
                if n not in visited:
                    dfs(n)


        for node in nodes:
            if node not in visited:
                dfs(node)
                components += 1

        return components