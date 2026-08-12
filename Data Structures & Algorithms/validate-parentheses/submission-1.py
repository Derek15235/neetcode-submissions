class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_stack = []
        parenthesis_map = {'(': ')', '[': ']', '{': '}'}
        
        for c in s:
            if c in parenthesis_map:
                parenthesis_stack.append(c)
            elif len(parenthesis_stack) == 0:
                return False
            else:
                recent_open = parenthesis_stack.pop()
                if c != parenthesis_map[recent_open]:
                    return False

        return len(parenthesis_stack) == 0
                
