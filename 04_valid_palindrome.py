# Leet Code 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def reverseString(self, s: str) -> bool:
        clean_text = ''.join(ch.lower() for ch in s if ch.isalnum()) # filter non-alphanum and lowercase
        return clean_text == clean_text [::-1]                       # check if string is equal to its reverse
    
    def twoPointers(self, s: str) -> bool:
        l, r= 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):                 # skip non-alphanumeric characters
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():    
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):                                           # check if character is alphanumeric
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
sol = Solution()
s = "A man, a plan, a canal: Panama"
print("Reverse String:", sol.reverseString(s))