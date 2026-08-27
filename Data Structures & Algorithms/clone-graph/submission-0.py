"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = {} # Key: Original, Value: Cloned Node
        def dfs(root):
            if root in clone:
                return clone[root]
            # Make clone of current 
            cloneNode = Node(root.val)
            clone[root] = cloneNode
            for neighbor in root.neighbors:
                dfs(neighbor)
                cloneNode.neighbors.append(clone[neighbor])
            return cloneNode
        return dfs(node)
            

        