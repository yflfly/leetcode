'''
122. 买卖股票的最佳时机 II
给你一个整数数组 prices ，其中prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润

给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
提示：
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i]<= 10 ^ 4

leetcode链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
'''


# 方法一：动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(2)] for j in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


'''
考虑到不能参与多笔交易，因此每天交易结束后只可能存在手里有一支股票或者没有股票的状态
dp[i][0]：表示第i天交易完成后手里没有股票的最大利润
dp[i][1]：表示第i天交易完成后手里持有一支股票的最大利润(i从0开始)
'''


# 使用2个一维数组表示dp
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp_0 = [0 for i in prices]  # 第i天手里没有股票
        dp_1 = [0 for i in prices]  # 第i天手里有股票
        dp_1[0] = -prices[0]
        for i in range(1, len(prices)):
            dp_0[i] = max(dp_0[i - 1], dp_1[i - 1] + prices[i])
            dp_1[i] = max(dp_1[i - 1], dp_0[i - 1] - prices[i])
        return dp_0[-1]


'''
讲解：

1）当天交易完之后手里没有股票可能有两种情况
一种是当天没有进行任何交易，又因为当天手里没有股票，所以当天没有股票的利润只能取前一天手里没有股票的利润。
一种是把当天手里的股票给卖了，既然能卖，说明手里是有股票的，所以这个时候当天没有股票的利润要取前一天手里有股票的利润加上当天股票能卖的价格。
这两种情况我们取利润最大的即可，所以可以得到
dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i]);


2）当天交易完之后手里持有股票也有两种情况
一种是当天没有任何交易，又因为当天手里持有股票，所以当天手里持有的股票其实前一天就已经持有了。
还一种是当天买入了股票，当天能买股票，说明前一天手里肯定是没有股票的，我们取这两者的最大值，所以可以得到
dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i]);

'''


# 方法二：代码优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n = len(prices)
        hold = -prices[0]  # 持有股票
        no_hold = 0  # 没持有股票
        for i in range(1, n):
            no_hold = max(no_hold, hold + prices[i])
            hold = max(hold, no_hold - prices[i])
        return no_hold  # 最后一天肯定是手里没有股票的时候利润才会最大


'''
上面计算的时候我们看到当天的利润只和前一天有关，没必要使用一个二维数组，只需要使用两个变量，
一个记录当天交易完之后手里持有股票的最大利润，一个记录当天交易完之后手里没有股票的最大利润
'''
