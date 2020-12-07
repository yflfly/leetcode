# coding:utf-8
'''
494. 目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
 
提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。

注意：给出的例子全是1，但其实可以为任意的正整数
'''


class Solution:
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        if total < S:
            return 0
        dp = [[0 for i in range(2 * total + 1)] for j in range(len(nums))]
        if nums[0] == 0:
            dp[0][total] = 2
        else:
            dp[0][total + nums[0]] = 1
            dp[0][total - nums[0]] = 1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                left, right = 0, 0
                if j - nums[i] >= 0:
                    left = j - nums[i]
                if j + nums[i] < 2 * total + 1:
                    right = j + nums[i]
                dp[i][j] = dp[i - 1][left] + dp[i - 1][right]
        return dp[-1][total + S]
