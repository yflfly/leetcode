# coding:utf-8
'''
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），
并返回该子数组所对应的乘积。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp_max = [1 for i in nums]
        dp_min = [1 for i in nums]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
        return max(dp_max)


# 用一个二维的数组合并两个dp为一个dp
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # dp
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        # dp init
        dp[0] = [nums[0], nums[0]]
        # dp
        for i in range(1, len(nums)):
            current, max_dp, min_dp = nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i]
            dp[i][0] = max(current, max_dp, min_dp)
            dp[i][1] = min(current, max_dp, min_dp)

        return max(max(dp))


'''
讲解：
解题思路 & 方法
和最大子数和题目相比，这个题目是乘法。那么，就可能出现，前面一个负数，乘以一个新的负数，得到一个大的正数。所以，我们需要保存一个最小值。

确定 dp[i] 的含义
1）此处我们设置两个 dp，一个 dp_max[i] 是我们的主 dp 数组，一个 dp_min 是我们的辅助 dp 数组。
2）dp_max[i] 表示以 nums[i] 为结尾的乘积最大子数组的乘积
3）dp_min[i] 表示以 nums[i] 为结尾的乘积最小子数组的乘积
确定状态转移方程
1）我们将大数组一步一步分为小数组，那么 dp 的最大乘积可能为
2）nums[i]、以 i-1 结尾的乘积最大子数组的乘积 dp_max[i] * nums[i]、以 i-1 结尾的乘积最小子数组的乘积 dp_min[i] * nums[i]
3）对于 dp_max ，取三者的 max；对于dp_min，取三者的 min
确定初始状态
1）初始化为数组第一个数 dp_max[0], dp_min[0] = nums[0], nums[0]
2）其余位置设置为 0

也可以用一个统一的二维数组将 dp_max ，dp_min 放入第一列和第二列

'''
