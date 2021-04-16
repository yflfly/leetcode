# coding:utf-8
'''
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。
示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：
输入：coins = [2], amount = 3
输出：-1
示例 3：
输入：coins = [1], amount = 0
输出：0
示例 4：
输入：coins = [1], amount = 1
输出：1
示例 5：
输入：coins = [1], amount = 2
输出：2
提示：
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [10001] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == 10001:
            return -1
        else:
            return dp[-1]


'''
完全背包问题：填满容量为amount的背包最少需要多少硬币
dp[i]：填满容量为i的背包最少需要多少硬币
初始化dp数组：因为硬币的数量一定不会超过amount，而amount<=10^4，因此初始化数组值为10001，dp[0]=0
转移方程：dp[i] = min(dp[i],dp[i-coin]+1),当前填满容量i最少需要的硬币 = min( 之前填满容量i最少需要的硬币, 填满容量i - coin 需要的硬币 + 1个当前硬币）
返回值：返回dp[amount]，如果dp[amount]的值为10001没有变过，说明找不到硬币组合，返回-1

复杂度分析
时间复杂度：O(n∗amount)
空间复杂度：O(amount)
'''
