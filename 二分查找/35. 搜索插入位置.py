# coding:utf-8
'''
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:
输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
示例 3:
输入: [1,3,5,6], 7
输出: 4
示例 4:
输入: [1,3,5,6], 0
输出: 0
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target == nums:
            return len(nums) - 1
        for i in range(len(nums) - 1):
            if target > nums[i] and target <= nums[i + 1]:
                return i + 1


# 二分法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            if nums[middle] < target:
                left = middle + 1
            if nums[middle] == target:
                return middle
        return left
