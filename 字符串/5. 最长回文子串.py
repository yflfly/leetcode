# coding:utf-8
'''
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：
输入：s = "cbbd"
输出："bb"
示例 3：
输入：s = "a"
输出："a"
示例 4：
输入：s = "ac"
输出："a"
'''


# 方法一：暴力求解法 leetcode运行时会出现 超出时间限制
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_len = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    if j - i > max_len:
                        max_len = j - i
                        res = s[i:j]
        return res


'''
复杂度分析：
时间复杂度：O(n^3)
空间复杂度：O(1)
'''
