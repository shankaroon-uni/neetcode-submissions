class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr = []
        used = set()

        def dfs():
            if len(curr) == len(nums):
                permutations.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                curr.append(nums[i])
                used.add(nums[i])
                dfs()
                curr.pop()
                used.remove(nums[i])

        dfs()
        return permutations