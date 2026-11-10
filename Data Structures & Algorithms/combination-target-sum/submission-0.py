class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        counting = []
        
        def dfs(i, diff):
            if i == len(nums):
                return
            if diff == 0:
                res.append(counting[:])
                return
            if diff < 0:
                return
                
    
            counting.append(nums[i])
            #res.append(counting[:])
            dfs(i,diff-nums[i])
            counting.pop()
            dfs(i+1, diff)
        dfs(0,target)
        return res

