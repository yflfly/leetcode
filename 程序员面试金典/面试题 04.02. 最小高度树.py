'''
面试题 04.02. 最小高度树
给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

示例:
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0
         / \
       -3   9
       /   /
     -10  5

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


'''
解题思路：
需要明确二叉树的定义：从节点的值来看简单来说就是：左子树<根<右子树
通过二叉搜索树的定义，我们可以知道其根节点必然是有序整数序列的中位数，对于长度为奇数的序列来说，很自然地取到中位数，对于长度为偶数的序列，根节点取右中位数。

由于是有序整数，那么在找到根节点后，我们可以将数组一分为二，其左侧必然是左子树，右侧必然是右子树。

最后再考虑一下终止条件，就是这样一直划分到数组为空。

参考网址：
https://leetcode-cn.com/problems/minimum-height-tree-lcci/solution/python-di-gui-jie-fa-by-tristangao/
'''
