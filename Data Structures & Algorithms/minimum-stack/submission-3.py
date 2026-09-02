class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minimum.append(val)
        if val <= self.minimum[-1]:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
