# coding:utf-8
'''
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        if root.left:
            root.left.val = root.val + root.left.val
        if root.right:
            root.right.val = root.val + root.right.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


'''
代码讲解网址：
https://leetcode-cn.com/problems/path-sum/solution/you-neng-dp-zai-yuan-er-cha-shu-shang-jin-xing-xiu/
'''
# 不对原来的树进行修改
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
'''
复杂度分析
时间复杂度：O(N)，其中N是树的节点数。对每个节点访问一次。
空间复杂度：O(H)，其中H是树的高度。空间复杂度主要取决于递归时栈空间的开销，最坏情况下，树呈现链状，空间复杂度为 O(N)。平均情况下树的高度与节点数的对数正相关，空间复杂度为O(logN)。
'''