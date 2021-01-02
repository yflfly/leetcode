'''
面试题 04.09. 二叉搜索树序列
从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉搜索树，输出所有可能生成此树的数组。

示例：
给定如下二叉树

        2
       / \
      1   3
返回：
[
   [2,1,3],
   [2,3,1]
]

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        res = []

        def findPath(cur, q, path):
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not q:
                res.append(path)
                return
            for i, nex in enumerate(q):
                newq = q[:i] + q[i + 1:]
                findPath(nex, newq, path + [nex.val])

        findPath(root, [], [root.val])
        return res


'''
讲解参考网址：
https://leetcode-cn.com/problems/bst-sequences-lcci/solution/15xing-dai-ma-by-suibianfahui/
'''
