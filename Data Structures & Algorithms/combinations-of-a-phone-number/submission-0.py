class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit = {
            "2":"abc", 
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}

        
        result = []
        current = ""
        if not digits:
            return []

        def dfs(i):
            nonlocal current 
            
            if i == len(digits):
                result.append(current)
                return
            for letter in digit[digits[i]]:
                current += letter
                dfs(i+1)
                current = current[:-1]
        dfs(0)
        return result