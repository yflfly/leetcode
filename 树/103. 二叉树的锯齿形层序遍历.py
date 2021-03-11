# coding:utf-8
'''
103. 二叉树的锯齿形层序遍历
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：
[
  [3],
  [20,9],
  [15,7]
]

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        tag = 0
        res = []
        while stack:
            tmp = []
            linshi = []
            tag += 1
            if tag % 2 == 0:
                for node in stack:
                    linshi.append(node.val)
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                linshi = linshi[::-1]
            else:
                for node in stack:
                    linshi.append(node.val)
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
            stack = tmp
            if linshi:
                res.append(linshi)
        return res
