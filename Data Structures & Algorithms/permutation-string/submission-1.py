class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = [0] * 26, [0] * 26
        l = 0

        for i in s1:
            index = ord(i) - ord('a')
            s1Count[index] += 1

        for r in range(len(s2)):
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if (r - l) == len(s1) - 1 and s1Count == s2Count:
                return True
            if (r - l) == len(s1) - 1:
                l_index = ord(s2[l]) - ord('a')
                s2Count[l_index] -= 1
                l += 1
        return False

            
