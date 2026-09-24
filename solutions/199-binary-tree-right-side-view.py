# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []

        def fun(root, l):
            if not root:
                return
            if l == len(ans):
                ans.append(root.val)
            fun(root.right, l+1)
            fun(root.left, l+1)

        fun(root, 0)
        return ans
