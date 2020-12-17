# coding:utf-8
'''
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def get_path(root, path):
            if root:
                path.append(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    get_path(root.left, path)
                    get_path(root.right, path)
        paths = []
        get_path(root, [])
        res = []
        for each in paths:
            he = 0
            for e in each:
                he += e
            if he == sum:
                res.append(each)

        return res