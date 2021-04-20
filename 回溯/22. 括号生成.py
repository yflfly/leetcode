'''
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1
输出：["()"]
提示：
1 <= n <= 8
'''


# 回溯法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(n, res, 0, 0, '')
        return res

    def backtrack(self, n, res, left, right, s):
        if right > left:  # 当前路径没有办法往下面走，退出条件之一
            return
        if left == n and right == n:  # 找到有效的括号，退出条件之一
            res.append(s)
            return
        if left < n:
            self.backtrack(n, res, left + 1, right, s + '(')
        if right < left:
            self.backtrack(n, res, left, right + 1, s + ')')


'''
条件：
l：左边括号的数量
r：右边括号的数量
l>= r 可以继续走下去
l<r 不可以继续走下去
l==r==n 获得一个满足条件的括号匹配对
空间复杂度：O(n)，除了答案数组之外，我们所需要的空间取决于递归栈的深度，每一层递归函数需要O(1) 的空间，最多递归2n层，因此空间复杂度为O(n)。

'''
