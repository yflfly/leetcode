'''
剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
'''


# 方法一：统计、比较 面试不建议这种方法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for each in nums:
            if each not in dict1:
                dict1[each] = 1
            else:
                dict1[each] += 1
        length = len(nums) // 2
        for each in dict1:
            if dict1[each] > length:
                return each


# 方法二：快速排序 时间超时
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def fast_order(start, end, nums):
            if start >= end:
                return
            minvalue = nums[start]
            low = start
            high = end
            while low < high:
                while low < high and nums[high] >= minvalue:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] <= minvalue:
                    low += 1
                nums[high] = nums[low]
            nums[low] = minvalue
            fast_order(start, low - 1, nums)
            fast_order(low + 1, end, nums)

        fast_order(0, len(nums) - 1, nums)
        return nums[len(nums) // 2]


# 快排  可以通过
'''
解题思路
随机选中一个数字，调整该数字的位置，使得所有比它小的数字在它的左边，所有比它大的数字在它右边；
排序后若该数字索引为n//2，则该数字即为中位数；
若索引小于n//2，在数字右边寻找新数；
若索引大于n//2，在数字左边寻找新数。
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        mid = n // 2
        index = self.quickSort(nums, left, right)
        while index != mid:
            if index > mid:
                right = index - 1
                index = self.quickSort(nums, left, right)
            else:
                left = index + 1
                index = self.quickSort(nums, left, right)
        return nums[index]

    def quickSort(self, nums, left, right):
        i, j = left, right
        key = nums[i]
        while i < j:
            while i < j and nums[j] > key:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] < key:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = key
        return i
