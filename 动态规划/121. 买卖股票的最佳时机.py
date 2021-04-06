# coding:utf-8
'''
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
示例 1:输入: [7,1,5,3,6,4]输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:输入: [7,6,4,3,1]输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''


class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        dp = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            min_ = min(prices[:i])
            if prices[i] > min_:
                dp[i] = prices[i] - min_
        return max(dp)


# min_的另外一种秋解方法
class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        dp = [0 for i in range(len(prices))]
        min_ = prices[0]
        for i in range(1, len(prices)):
            # min_ = min(prices[:i])
            if prices[i] > min_:
                dp[i] = prices[i] - min_
            else:
                min_ = prices[i]
        return max(dp)


prices = [7, 1, 5, 3, 6, 4]
dp = [0 for _ in prices]
for i in range(1, len(prices)):
    if prices[i] > min(prices[:i]):
        dp[i] = prices[i] - min(prices[:i])
print(max(dp))  # 5
