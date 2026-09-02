class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []

        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            second = i + 1
            third = len(nums) - 1
            while second < third :
                temp = sorted_nums[i] + sorted_nums[second] + sorted_nums[third]
                if temp == 0:
                    output.append([sorted_nums[i] , sorted_nums[second] , sorted_nums[third]])
                    second += 1
                    third -= 1
                    while second < third and sorted_nums[second] == sorted_nums[second - 1]:
                        second += 1 
                elif temp > 0:
                    third -= 1
                elif temp < 0:
                    second += 1

        return output