# coding:utf-8
'''
713. 乘积小于K的子数组
给定一个正整数数组 nums。
找出该数组内乘积小于 k 的连续的子数组的个数。
示例 1:
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        res = 0
        left = 0
        n = len(nums)
        prod = 1
        for right in range(n):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right-left+1
        return res
'''
讲解的网址：
https://leetcode-cn.com/problems/subarray-product-less-than-k/solution/hua-dong-chuang-kou-fa-by-jia-zhi-tong-1/
'''