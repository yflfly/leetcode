'''
面试题28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        right = []
        left = []
        if not root:
            return True
        count_left(root.left, left)
        count_rigth(root.right, right)
        if left == right:
            return True
        else:
            return False


def count_left(t, list1):
    if t:
        list1.append(t.val)
        count_left(t.left, list1)
        count_left(t.right, list1)
    else:
        list1.append('null')


def count_rigth(t1, list2):
    if t1:
        list2.append(t1.val)
        count_rigth(t1.right, list2)
        count_rigth(t1.left, list2)

    else:
        list2.append('null')


#
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(p1, p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val == p2.val:
                return isSame(p1.left, p2.right) and isSame(p1.right, p2.left)
            return False

        if not root:
            return True
        if not root.left and root.right:
            return False
        if root.left and not root.right:
            return False
        return isSame(root.left, root.right)
