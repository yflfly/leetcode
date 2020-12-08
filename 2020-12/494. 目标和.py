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

class Solution2:
    def findTargetSumWays(self, nums, S) -> int:
        """
        （1）思路：动态规划
                我们用 dp[i][j] 表示用数组中的前 i 个元素，组成和为 j 的方案数。考虑第 i 个数 nums[i]，它可以被添
            加 + 或 - ，那么从dp[i-1][m] —> dp[i][j] 可以在 dp[i-1][m]的基础上加上 nums[i] 或者减去 nums[i]，
            因此状态转移方程如下：
                dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j + nums[i]]
        （2）复杂度：
            - 时间复杂度：O（N * sums） 其中 N 是数组 nums 的长度
            - 空间复杂度：O（N * sums）
        """
        import collections
        # 获取数组长度和数组和的最大值
        array_length, max_sum = len(nums), sum(nums)
        # 定义和初始化dp数组
        # 因为该数组所能组成的值的区间为[min_sum, max_sum]，即一共有 max_sum - min_sum + 1 种值
        # 但是为了方便，可以直接定义为dict的形式，这样就可以一直增加key而不需要去计算dp数组第二维的长度，同时不用管下标为
        # 负数的情况，直接将下标转化为dict中的key
        # 这样不存在的key，也会默认是0
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        # 之所以dp[0][-nums[0]] 使用 += 1 而不是直接赋值1，是为了处理nums[0]就等于0的情况
        # 如果nums[0]， 那么dp[0][0] = 2 而不是 1
        dp[0][nums[0]] = 1
        dp[0][-nums[0]] += 1
        # 遍历nums数组，更行dp数组的值
        for i in range(1, array_length):
            for j in range(-max_sum, max_sum+1):
                # 状态转移方程
                # 当dp[i][j]不等于的0的时候，代表至少存在一种方法得到j值
                dp[i][j] = dp[i - 1].get(j + nums[i], 0) + dp[i - 1].get(j - nums[i], 0)
        return dp[-1][S]

