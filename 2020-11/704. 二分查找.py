# coding:utf-8
'''
704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 
提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。

'''
# 下面是本人的代码：
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle+1
            else:
                right = middle-1
        return -1

''''
# 别人的代码
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0;
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if target == nums[mid]: return mid
            if target < nums[mid]:
                right = mid - 1
            else :
                left = mid + 1
        return -1

复杂度分析

时间复杂度: O(logn)
空间复杂度: O(1)
'''