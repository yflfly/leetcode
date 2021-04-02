'''
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：[3,2,3]
输出：3
示例 2：
输入：[2,2,1,1,1,2,2]
输出：2
相关标签  位运算、数组、分治算法
'''


# 方法一：字典统计
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        middle = len(nums) // 2
        dict1 = {}
        for each in nums:
            if each not in dict1:
                dict1[each] = 1
            else:
                dict1[each] += 1
        for each in dict1:
            if dict1[each] > middle:
                return each


# 方法二：摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = 0
        count_a = 0
        for each in nums:
            if each == a:
                count_a += 1
                continue
            if count_a == 0:
                a = each
                count_a = 1
            count_a -= 1
        count_a = 0
        for each in nums:
            if each == a:
                count_a += 1
        if count_a > len(nums) / 2:
            return a
        else:
            return 0
