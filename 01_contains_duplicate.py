# LeetCode Problem - 217: Contains Duplicate
class Solution:
    def bruteForce(self, nums: list[int]) -> bool: # Time: O(n^2), Space: O(1)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    def sorting(self, nums: list[int]) -> bool: # Time: O(n log n), Space: O(1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    def hashset(self, nums: list[int]) -> bool: # Time: O(n), Space: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def builtin(self, nums: list[int]) -> bool: # Time: O(n), Space: O(n)
        return len(nums) != len(set(nums))

n = [1, 2, 4, 2, 5, 6]
sol = Solution()
print(sol.bruteForce(n))
print(sol.sorting(n))
print(sol.hashset(n))
print(sol.builtin(n))