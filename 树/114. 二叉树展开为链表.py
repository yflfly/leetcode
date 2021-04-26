'''
114. 二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
示例 2：
输入：root = []
输出：[]
示例 3：
输入：root = [0]
输出：[0]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tmp_list = []

        def preorder(root):
            if root:
                tmp_list.append(root)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        for i in range(1, len(tmp_list)):
            pre = tmp_list[i - 1]
            cur = tmp_list[i]
            pre.left = None
            pre.right = cur


'''
将二叉树展开为单链表之后，单链表得节点顺序即为二叉树得前序遍历访问各个节点得顺序
'''
