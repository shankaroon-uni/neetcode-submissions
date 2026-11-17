class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        currentSum = []
        candidates.sort()
        def dfs(start, diff):
            if diff == 0:
                res.append(currentSum[:])
                return

            if diff < 0:
                return

            for i in range(start, len(candidates)):

                if i>start and candidates[i] == candidates[i-1]:
                    continue

                currentSum.append(candidates[i])

                dfs(i + 1, diff - candidates[i])

                currentSum.pop()
        dfs(0,target)
        return res