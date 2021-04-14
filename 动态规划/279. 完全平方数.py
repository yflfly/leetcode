'''
279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9
'''


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]


'''
dp[i]：表示完全平方和为i的最小个数
初始状态：dp[i]=i 即最坏情况下 1+1+1……+1 共i个1，其中dp[0]=0
状态转移方程：dp[i] = min(dp[i],dp[i-j*j]+1)
i可分解成j*j+(i-j*j),dp[i]=1+dp[i-j*j],因为j*j多加一次
'''
