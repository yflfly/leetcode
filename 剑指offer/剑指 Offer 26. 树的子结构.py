# codin:utf-8
'''
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：
0 <= 节点个数 <= 10000

'''
# Definition for a binary tree node.
class Solution:
    def check(self, s, t):  # 这里 t 可能为空
        if not t:
            return True
        if not s:
            return False

        return s.val == t.val and self.check(s.left, t.left) and self.check(s.right, t.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B: return False
        return self.check(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

