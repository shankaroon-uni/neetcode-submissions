class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        nodes = {i:[] for i in range(n)}

        for root, node in edges:
            nodes[root].append(node)
            nodes[node].append(root)

        def dfs(node, parent):
            if node in visited:
                return False
                
            visited.add(node)
            for n in nodes[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            return True

        
        return dfs(0, -1) and len(visited) == n