class MinStack:

    def __init__(self):
        self.allStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.allStack.append(val)

    def pop(self) -> None:
        res = self.allStack.pop()
        if res == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.allStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
