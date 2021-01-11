# coding:utf-8
'''
最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3 or not nums:
            return []
        nums_sorted = sorted(nums)
        n = len(nums)
        res = nums_sorted[0] + nums_sorted[1] + nums_sorted[2]
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum1 = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
                if abs(target - sum1) < abs(target - res):
                    res = sum1
                if sum1 > target:
                    right -= 1
                elif sum1 < target:
                    left += 1
                else:
                    return res
        return res
