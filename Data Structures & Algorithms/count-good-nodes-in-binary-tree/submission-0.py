# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, biggestSoFar):
            nonlocal res
            if not root:
                return
            newBiggest = biggestSoFar
            if root.val >= biggestSoFar:
                res += 1
                newBiggest = root.val
            dfs(root.left, newBiggest)
            dfs(root.right, newBiggest)

        dfs(root, -101)
        return res