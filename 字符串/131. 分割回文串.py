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

考查标签：深度优先搜索、动态规划、回溯算法
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, state = [], []

        def check(str1):
            if str1 != str1[::-1]:
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
