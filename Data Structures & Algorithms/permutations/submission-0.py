class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr = []
        used = set()

        def dfs(start):
            if start > len(nums):
                return
            if len(curr) == len(nums):
                permutations.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                curr.append(nums[i])
                used.add(nums[i])
                dfs(i+1)
                curr.pop()
                used.remove(nums[i])

        dfs(0)
        return permutations