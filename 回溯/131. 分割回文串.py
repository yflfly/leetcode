# coding:utf-8
'''
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

'''
四步：全局变量、参数设计、完成条件、递归过程。
全局变量：该题目要找到可分割的方案，最终结果形式上是：[[],[],[],...]
参数设计：（1）状态变量：当前是回文的字符串（2）条件变量：剩余待搜索的字符串，当字符串长度为0，则搜索完毕。
完成条件：剩余字符串长度为0。
递归过程：在剩余字符串中遍历，如果该串为回文 就 进入下次递归，如果非回文 就 继续搜索下一个串。

代码讲解网址：https://zhuanlan.zhihu.com/p/112926891
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  # 定义全局变量保存最终结果
        state = []  # 定义状态变量保存当前状态

        def check_str(i):  # 检查字符串列表是否为回文
            if i != i[::-1]:
                return False
            return True

        def back(state, s):
            if len(s) == 0:  # 状态满足最终要求
                res.append([i for i in state])  # 加入结果
                return
            # 主要递归过程，一般是带有 循环体 或者 条件体
            for i in range(0, len(s)):
                if check_str(s[:i + 1]):
                    # python的状态传递写法，列表 state+[xxx]，字符串 state+"xxx"
                    back(state + [s[:i + 1]], s[i + 1:])

        back(state, s)
        return res


def own(s):
    res = []
    state = []

    def check(i):
        if i != i[::-1]:
            return False
        return True

    def back(state, s):
        if len(s) == 0:
            res.append([e for e in state])
            return
        for i in range(0, len(s)):
            if check(s[:i + 1]):
                back(state + [s[:i + 1]], s[i + 1:])

    back(state, s)
    return res
