class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        s_count = {}
        have, need = 0, len(t_count)
        res = [-1, -1]
        res_len = float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            s_count[char] = s_count.get(char, 0) + 1

            if char in t_count and s_count[char] == t_count[char]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                left_char = s[l]
                s_count[left_char] -= 1
                if left_char in t_count and s_count[left_char] < t_count[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""