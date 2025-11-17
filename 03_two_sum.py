# Leet Code 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def bruteForce(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range (i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []


nums = [3,7,2,4,4]
target = 8
sol = Solution()
print(sol.bruteForce(nums, target))