class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        running = []

        def dfs(i):
            if i >= len(nums):
                return
            num = nums[i]
            dfs(i+1)
            running.append(num)
            res.append(running.copy())
            dfs(i+1)
            running.pop()

        dfs(0)

        return res