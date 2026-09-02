class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, output = 0, 0, 0
        max_freq = 0
        freq_map = defaultdict()
        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(max_freq, freq_map[s[r]])
            window = r - l + 1
            replacement = window - max_freq
            if replacement <= k:
                output = max(window, output)
            else:
                freq_map[s[l]] = freq_map.get(s[l], 0) - 1
                l += 1

        return output
