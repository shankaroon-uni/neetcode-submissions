class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        permutations = []
        curr = []

        def dfs(open_count,closed_count):
            if (open_count + closed_count) == 2*n:
                permutations.append("".join(curr))
                return
            if open_count < n:
                curr.append("(")
                dfs(open_count +1, closed_count)
                curr.pop()
            if closed_count < open_count:
                curr.append(")")
                dfs(open_count, closed_count+1)
                curr.pop()
            

        dfs(0,0)
        return permutations