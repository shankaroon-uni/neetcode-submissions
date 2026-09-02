class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if len(stack) > 1 and (i == "+" or i == "*" or i == "-" or i == "/"):
                one = int(stack.pop())
                two = int(stack.pop())
                if i == "+":
                    stack.append(one+two)
                elif i == "*":
                    stack.append(one*two)
                elif i == "-":
                    stack.append(two-one)
                elif i == "/":
                    stack.append(int(two/one))
            else:
                stack.append(i)

        if len(tokens) == 1:
            return int(tokens[0])
        else:
            return stack[0]