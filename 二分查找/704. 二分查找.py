# coding:utf-8
'''
704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，
如果目标值存在返回下标，否则返回 -1。
示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = left+(right-left)//2
            if target == nums[middle]:
                return middle
            if nums[middle] < target:
                left = middle+1
            else:
                right = middle-1
        return -1
'''
复杂度分析
时间复杂度：O(logN)
空间复杂度：O(1)
'''
