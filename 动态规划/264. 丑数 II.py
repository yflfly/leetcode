'''
264. 丑数 II
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。
示例 1：
输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
示例 2：
输入：n = 1
输出：1
解释：1 通常被视为丑数。
'''


# 动态规划
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n + 1):
            t2 = dp[p2] * 2
            t3 = dp[p3] * 3
            t5 = dp[p5] * 5
            dp[i] = min(t2, t3, t5)
            if t2 == dp[i]:
                p2 += 1
            if t3 == dp[i]:
                p3 += 1
            if t5 == dp[i]:
                p5 += 1
        return dp[n]
