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


# 方法二：快速排序
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
