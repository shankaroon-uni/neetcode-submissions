class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr = []
        nums.sort()

        def dfs(start):
            permutations.append(curr[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                
                dfs(i + 1)
                curr.pop()

        dfs(0)
        return permutations