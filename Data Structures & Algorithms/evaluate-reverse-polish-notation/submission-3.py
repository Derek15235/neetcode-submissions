class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operators:
                numStack.append(int(token))
            else:
                right = numStack.pop()
                left = numStack.pop()
                if token == "+":
                    numStack.append(left + right)
                elif token == "-":
                    numStack.append(left - right)
                elif token == "*":
                    numStack.append(left * right)
                else:
                    res = abs(left) // abs(right)
                    if (left < 0) != (right < 0):
                        numStack.append(-res)
                    else:
                        numStack.append(res)
        return numStack[0]


            