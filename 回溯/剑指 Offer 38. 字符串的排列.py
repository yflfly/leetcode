# coding:utf-8
'''
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
'''


class Solution:
    def permutation(self, s: str) -> List[str]:
        length = len(s)
        if length == 1:
            return [s]  # 边界
        else:
            res = []
            for i in range(length):
                ch = s[i]  # 取出s中每一个字符
                rest = s[:i] + s[i + 1:]
                for x in self.permutation(rest):  # 递归
                    res.append(ch + x)  # 将ch 和子问题的解依次组合
        return list(set(res))


class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue  # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res


'''
全局变量：res = []
参数设计：（1）状态变量：当前组成的字符排列（2）条件变量：剩余的备选字符。
完成条件：当前状态没有被组成，就加入到res；被组成过，就停止搜索。
递归过程：加入当前元素进入下一次递归。
'''


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []  # 定义全局变量保存最终结果
        state = ""  # 定义状态变量保存当前状态
        exist = set()  # 定义条件变量（一般条件变量就是题目直接给的参数）

        def back(state, s):
            if state in exist:  # 不满足合法条件（可以说是剪枝）
                return
            elif len(s) == 0:  # 状态满足最终要求
                res.append(state)  # 加入结果
                exist.add(state)
                return
                # 主要递归过程，一般是带有 循环体 或者 条件体
            for i in range(len(s)):  # 满足执行条件
                back(state + s[i], s[:i] + s[i + 1:])

        back(state, s)
        return res
