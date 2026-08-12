class MinStack(object):

    def __init__(self):
        self.stack = []
        # Key: index, Val: min up to the index
        self.minVals = {}

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        idx = len(self.stack) - 1
        if idx > 0:
            self.minVals[idx] = min(value, self.minVals[idx - 1])
        else:
            self.minVals[idx] = value
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]
        
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVals[len(self.stack) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()