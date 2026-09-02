class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "-":
                one , two = stack.pop(), stack.pop()
                stack.append(two - one)
            elif i == "/":
                one , two = stack.pop(), stack.pop()
                stack.append(int(two/one))
            else:
                stack.append(int(i))
        return stack[0]