'''
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 一棵高度平衡二叉树定义为：一个二叉树每个节点的左右两个子树的高度差的绝对值不超过1。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def count(root):
            if not root:
                return 0
            left = count(root.left)
            if left == -1:  # 判断左子树是否平衡
                return -1
            right = count(root.right)
            if right == -1:  # 判断右子树是否平衡
                return -1
            # 到这里说明左右子树都平衡，那么就判断总的是否平衡
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        res = count(root)
        if res == -1:
            return False
        else:
            return True
'''
复杂度分析：
时间复杂度O(N)： N 为树的节点数；最差情况下，需要递归遍历树的所有节点。
空间复杂度O(N)： 最差情况下（树退化为链表时），系统递归需要使用O(N)的栈空间。
'''