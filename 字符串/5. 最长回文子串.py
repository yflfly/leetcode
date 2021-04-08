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


# 方法二：动态规划法 leetcode运行时同样会出现 超出时间限制
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        ans = ''
        # 枚举子串的长度k+1
        for k in range(n):
            # 枚举子串的起始位置i，这样可以通过j=i+k得到子串的从结束位置
            for i in range(n):
                j = i + k
                if j >= n:
                    break
                if k == 0:
                    dp[i][j] = True
                elif k == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and k + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


'''
代码讲解网址：
https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
对于一个子串而言，如果它时回文串，并且长度大于2，那么将它首尾的两个字母去除之后，它仍然时个回文串，例如‘ababa’，若知道‘bab’时回文串，那么‘ababa’一定是回文串，这是因为它的首尾两个字母都是‘a’
复杂度分析：
时间复杂度：O(n^2)，其中n是字符串的长度。动态规划的状态总数为O(n^2)对于每个状态，我们需要转移的时间为O(1)。
空间复杂度：O(n^2)，即存储动态规划状态需要的空间。

'''
