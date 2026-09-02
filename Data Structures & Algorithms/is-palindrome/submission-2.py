class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while end > start:
            while start < end and not s[end].isalnum():
                end -= 1
            while start < end and not s[start].isalnum():
                start += 1
            if s[end].lower() != s[start].lower():
                return False
            end -= 1
            start += 1
        
        return True