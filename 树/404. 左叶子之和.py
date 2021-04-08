'''
404. 左叶子之和
计算给定二叉树的所有左叶子之和。
示例：
    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        res = 0
        while stack:
            tmp = []
            for node in stack:
                if node.left:
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
        return res