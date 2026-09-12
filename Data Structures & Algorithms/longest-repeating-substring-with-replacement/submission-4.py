class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, output = 0, 0
        hashmap = {}
        letter = s[0]
        maxf = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxf = max(maxf, hashmap[s[r]])
            while (r-l + 1) - maxf > k:
                hashmap[s[l]] = hashmap.get(s[l], 0) - 1
                l += 1
        return r - l + 1