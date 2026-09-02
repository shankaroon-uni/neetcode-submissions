class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_s = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for i in s:
            if i in dict_s:
                if stack and dict_s[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack