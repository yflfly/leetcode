'''
501. 二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
假定 BST 有如下定义：
结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法一：获取每个值，使用字典进行统计
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return
        dic = {}
        stack = [root]
        while stack:
            tmp = []
            for node in stack:
                if node.val not in dic:
                    dic[node.val] = 1
                else:
                    dic[node.val] += 1
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
        max_1 = 0
        res = []
        for key in dic:
            if dic[key] > max_1:
                max_1 = dic[key]
                res = [key]
            elif dic[key] == max_1:
                res.append(key)
        return res
