'''
括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

考查标签：字符串、回溯算法
'''


class Solution(object):
    def generateParenthesis(self, n):
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')


'''
回溯法的代码套路是使用两个变量：res和path,res表示最终的结果,path保存已经走过的路径。如果搜到一个状态满足题目要求，就把path放到res中
代码后面的判断条件都是 if，而不是 elif，因为是满足两个条件的任意一个就可以继续向下搜索，而不是同时只能满足其中的一个。

讲解参考网址：
https://leetcode-cn.com/problems/generate-parentheses/solution/ru-men-ji-bie-de-hui-su-fa-xue-hui-tao-lu-miao-don/
'''
