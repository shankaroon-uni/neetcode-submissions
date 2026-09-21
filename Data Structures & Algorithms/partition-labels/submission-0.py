class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = {}
        for x in range(len(s)):
            seen[s[x]] = x
        output = []
        previous = -1
        last = 0
        for i in range(len(s)):
            last = max(last,seen[s[i]])
            if i == last:
                output.append(last - previous) 
                previous = last

        return output