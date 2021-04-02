'''
334. 递增的三元子序列
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
示例 1：
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
示例 2：
输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组
示例 3：
输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
'''


class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == 3:
                        return True
        return False




class Solution(object):
    def increasingTriplet(self, nums):
        small, mid = float('inf'), float('inf')
        for x in nums:
            if x <= small:
                small = x
            elif x <= mid:
                mid = x
            elif x > mid:
                return True
        return False

'''
代码来源网址：
https://leetcode-cn.com/problems/increasing-triplet-subsequence/solution/python-di-zeng-zi-xu-lie-he-tan-xin-by-s-vvs2/
'''
