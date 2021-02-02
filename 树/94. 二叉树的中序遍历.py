# coding:utf-8
'''
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：
输入：root = []
输出：[]
示例 3：
输入：root = [1]
输出：[1]
示例 4：
输入：root = [1,2]
输出：[2,1]
示例 5：
输入：root = [1,null,2]
输出：[1,2]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 方法一 递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
'''
递归遍历太简单了
前序遍历：打印 - 左 - 右
中序遍历：左 - 打印 - 右
后序遍历：左 - 右 - 打印
题目要求的是中序遍历，那就按照 左-打印-右这种顺序遍历树就可以了，递归函数实现

终止条件：当前节点为空时
函数内：递归的调用左节点，打印当前节点，再递归调用右节点
时间复杂度：O(n)
空间复杂度：O(h)，h是树的高度
'''

# 方法二 迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res

'''
递归的调用过程是不断往左走，当左边走不下去了，就打印节点，并转向右边，然后继续这个过程，可以使用栈来模拟上面的调用过程

'''

''''
讲解的网址：
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/

'''

