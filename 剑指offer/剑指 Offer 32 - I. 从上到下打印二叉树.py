# coding:utf-8
'''
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回：
[3,9,20,15,7]
'''

'''
方法讲解：
题目要求二叉树从上至下打印(即按层打印)，又称为二叉树的广度优先搜索(BFS)
BFS通常是借助队列的先入先出特性来实现(在python中，也可以用列表进行存储，按照要求进行存储节点的顺序)

算法流程：
S1：特例处理： 当树的根节点为空，则直接返回空列表 [] ；
S2：初始化： 打印结果列表 res = [] ，包含根节点的队列 queue = [root] ；
S3：BFS 循环： 当队列 queue 为空时跳出；
    S3-1：出队： 队首元素出队，记为 node；
    S3-2：打印： 将 node.val 添加至列表 tmp 尾部；
    S3-3：添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue ；
注意：先进左子树，再进右子树
'''


# python队列实现
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


# python列表实现
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        stack = [root]
        while stack:
            tmp = []
            for node in stack:
                res.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
        return res
