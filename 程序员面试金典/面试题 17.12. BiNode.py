# coding:utf-8
'''
面试题 17.12. BiNode
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
返回转换后的单向链表的头节点。
注意：本题相对原题稍作改动
示例：
输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        self.pre = self.ans = TreeNode(-1)

        def dfs(root):
            if not root: return
            dfs(root.left)
            root.left = None
            self.pre.right = root
            self.pre = root
            dfs(root.right)

        dfs(root)
        return self.ans.right


'''
知识点：
对于一个二叉查找树，其中中序遍历结果是一个有序数组
递归与迭代的区别
递归：重复调用函数自身实现循环称为递归； 迭代：利用变量的原值推出新值称为迭代，或者说迭代是函数内某段代码实现循环；
'''
