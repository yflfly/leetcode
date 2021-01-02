'''
面试题 04.03. 特定深度节点链表
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。
示例：
输入：[1,2,3,4,5,null,7,8]

        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8
输出：[[1],[2,3],[4,5,7],[8]]

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        stack = [tree]
        res = []
        while stack:
            tmp = []
            for i in range(len(stack)):
                if stack[i].left:
                    tmp.append(stack[i].left)
                if stack[i].right:
                    tmp.append(stack[i].right)
                if i == 0:
                    head = ListNode(stack[i].val)
                    start = head
                else:
                    start.next = ListNode(stack[i].val)
                    start = start.next
            stack = tmp
            res.append(head)
        return res
