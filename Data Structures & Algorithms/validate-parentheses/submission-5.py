class Solution:
    def isValid(self, s: str) -> bool:
        # Key: Open, Value: Closed
        parentheses = {'(': ')', '{': '}', '[': ']'}
        parenStack = []
        for c in s:
            if c in parentheses:
                parenStack.append(c)
            else:
                if not parenStack:
                    return False
                
                nearestOpen = parenStack.pop()
                if c != parentheses[nearestOpen]:
                    return False
        return not parenStack