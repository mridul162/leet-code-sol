# Leet Code 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram_sorting(self, s: str, t: str) -> bool: # Time: O(nlogn+mlogm), Space: O(n+m)
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram_hashMap(self, s: str, t: str) -> bool: # Time: O(n+m), Space: O(1)
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[s[i]] = 1 + countT.get(s[i], 0)
        return countS == countT

    def isAnagram_hashTable(self, s: str, t: str) -> bool: # Time: O(n+m), Space: O(1)
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1
        for val in count:
            if val !=0:
                return False
        return True


anagram = Solution()
s = "mridul"
t= "drimul"

print(anagram.isAnagram_sorting(s,t))
print(anagram.isAnagram_hashMap(s,t))
print(anagram.isAnagram_hashTable(s,t))