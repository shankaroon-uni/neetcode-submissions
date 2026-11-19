class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []
        
        def dfs(start):
            if start == len(s):
                res.append(current[:])
                return
            for i in range(start,len(s)):
                substring = s[start:i + 1]
                if  substring == substring[::-1]:
                    current.append(substring)
                    dfs(i+1)
                    current.pop()
            

        dfs(0)
        
        return res

