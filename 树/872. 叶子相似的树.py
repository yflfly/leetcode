'''
872. 叶子相似的树
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。
如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
示例 1：
输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
输出：true
示例 2：
输入：root1 = [1], root2 = [1]
输出：true
示例 3：
输入：root1 = [1], root2 = [2]
输出：false
示例 4：
输入：root1 = [1,2], root2 = [2,2]
输出：true
示例 5：
输入：root1 = [1,2,3], root2 = [1,3,2]
输出：false
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.val_arr = list()

        def getLeaf(root: TreeNode):
            if root.left:
                getLeaf(root.left)
            if root.right:
                getLeaf(root.right)
            if not root.left and not root.right:
                self.val_arr.append(root.val)

        getLeaf(root1)
        val1 = self.val_arr
        self.val_arr = list()
        getLeaf(root2)
        val2 = self.val_arr
        return val1 == val2


'''
解题思路
本题需要注意的是，题目中的序列是考虑顺序的，因此如果单纯使用层序遍历的方式来遍历二叉树（也就是采用迭代的方式，一层层的将二叉树的值 append 进结果数组），那么序列的顺序很可能会不一样（[1,2,3] & [1,3,2]），这样就无法进行序列上的判断，只能进行值上的判断。因此考虑使用递归（深度优先遍历）的方式，来解题。
首先定义一个 leafSimilar() 内部的全局变量列表 self.val_arr，构建用来进行深度遍历的函数 getLeaf()，其作用就是深度遍历来寻找叶子节点，当找寻到叶子节点之后，将节点值 append 进之前定义好的全局变量 self.val_arr。思路非常简单，最后只需要比较两个结果数组是否相同就好。
'''
