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
                if not stack or dict_s[i] != stack.pop():
                    return False
            else:
                stack.append(i)

        return not stack