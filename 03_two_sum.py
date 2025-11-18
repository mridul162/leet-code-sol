# Leet Code 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def bruteForce(self, nums: list[int], target: int) -> list[int]:    # Time Complexity: O(n^2), Space Complexity: O(1)
        for i in range(len(nums)-1):
            for j in range (i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []
    
    def sorting(self, nums: list[int], target: int) -> list[int]:       # Time Complexity: O(n log n), Space Complexity: O(n)
        numsIndex = [(n,i) for i,n in enumerate (nums)]                 # create list of tuples (num, index)
        numsIndex.sort()
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            currentSum = numsIndex[left][0] + numsIndex[right][0]
            if currentSum == target:
                return [min(numsIndex[left][1], numsIndex[right][1]),
                        max(numsIndex[left][1], numsIndex[right][1])]   # return indices in ascending order
            elif currentSum < target:                                   # need a larger sum
                left += 1
            else:                                                       # need a smaller sum
                right -= 1 
        return []
    
    def hashMap(self, nums: list[int], target: int) -> list[int]:       # Time Complexity: O(n), Space Complexity: O(n)
        prevMap = {}
        for i, n in enumerate (nums):                                   # enumerate gives both index and value
            diff = target - n                                           # calculate the difference needed
            if diff in prevMap:
                return [prevMap[diff], i]                               # return indices
            prevMap[n] = i                                              # store number and its index
        return []
    
    
    

nums = [3,7,2,4,1]
target = 8
sol = Solution()
print("Brute Force:",sol.bruteForce(nums, target))
print("Sorting:",sol.sorting(nums, target))
print("Hash Map:",sol.hashMap(nums, target))