'''
673. 最长递增子序列的个数
给定一个未排序的整数数组，找到最长递增子序列的个数。
示例 1:
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
'''


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        dp = [1] * n  # 到nums[i]为止的最长递增子序列长度
        count = [1] * n  # 到nums[i]为止的最长递增子序列个数
        max_length = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            max_length = max(max_length, dp[i])

        res = 0
        for i in range(n):
            if dp[i] == max_length:
                res += count[i]
        return res


'''
复杂度分析
时间复杂度：O(n^2)
空间复杂度：O(n)
'''
