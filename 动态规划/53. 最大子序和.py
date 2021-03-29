# coding:utf-8
'''
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = tempSum = nums[0]
        for num in nums[1:]:
            tempSum = max(num, num + tempSum)
            maxSum = max(maxSum, tempSum)
        return maxSum


# 动态规划
class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0 for i in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


nums = [2, -1, 1, 2]
a = Solution()
print(a.maxSubArray(nums))
