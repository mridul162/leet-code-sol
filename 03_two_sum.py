# Leet Code 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def bruteForce(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,(len(nums)-1)):
            for j in range (1, len(nums)):
                if i!=j and nums[i]+nums[j] == target:
                    return sorted([i,j])


nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.bruteForce(nums, target))