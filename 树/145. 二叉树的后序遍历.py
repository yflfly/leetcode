# coding:utf-8
'''
145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        dfs(root)
        return res


# 非递归的方法
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack = [root]
        res = []
        while stack:
            s = stack.pop()
            res.append(s.val)
            if s.left:  # 与前序遍历相反
                stack.append(s.left)
            if s.right:
                stack.append(s.right)
        return res[::-1]


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res


'''
官方讲解：
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/bang-ni-dui-er-cha-shu-bu-zai-mi-mang-che-di-chi-t/
'''

'''
值得看的讲解网址：
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/bian-li-tong-jie-by-long_wotu/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []  # 用来存储后序遍历节点的值
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)  # 第一次入栈的是根节点
                # 判断当前节点的左子树是否存在，若存在则持续左下行，若不存在就转向右子树
                node = node.left if node.left is not None else node.right
            # 循环结束说明走到了叶子节点，没有左右子树了，该叶子节点即为当前栈顶元素，应该访问了
            node = stack.pop()  # 取出栈顶元素进行访问
            res.append(node.val)  # 将栈顶元素也即当前节点的值添加进res
            # （下面的stack[-1]是执行完上面那句取出栈顶元素后的栈顶元素）
            if stack and stack[-1].left == node:  # 若栈不为空且当前节点是栈顶元素的左节点
                node = stack[-1].right  # 则转向遍历右节点
            else:
                node = None  # 没有左子树或右子树，强迫退栈
        return res

'''
后序遍历比前序遍历更难一点。
因为前序遍历可以直接把当前非叶子节点从栈顶弹出，然后把它的子节点再压栈。
但是后序遍历需要先输出子节点再输出父节点，所以如果当前节点不是叶子节点那么就不能把它弹出。
但是如果不弹出，下次它出现在栈顶的时候就不知道它是否已经被遍历过了。

改进的方法就是，如果当前节点不是叶子节点，那么我把它的子节点保存起来，再把这个节点的子节点置为None。
然后按照[root, right, left]的顺序压回栈中。
这样当下次遍历到它的时候，程序会把它当作叶子节点直接输出~~

'''