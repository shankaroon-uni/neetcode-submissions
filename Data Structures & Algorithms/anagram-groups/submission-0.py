class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for i in strs:
            sorted_key = "".join(sorted(i))
            if sorted_key in output:
                output[sorted_key].append(i)
            else:
                output[sorted_key] = [i]

        return list(output.values())
