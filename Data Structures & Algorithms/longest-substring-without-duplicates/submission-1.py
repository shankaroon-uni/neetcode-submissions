class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_output = 0
        current = set()
        while r < len(s):
            while s[r] in current:
                current.remove(s[l])
                l += 1
            output = r - l + 1
            if output > max_output:
                max_output = output
    
            current.add(s[r])
            r += 1
        return max_output