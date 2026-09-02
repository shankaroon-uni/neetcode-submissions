class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for i in strs:
            sorted_key = "".join(sorted(i))
            output[sorted_key].append(i)
        return list(output.values())