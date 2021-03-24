'''
229. 求众数 II
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
示例 1：
输入：[3,2,3]
输出：[3]
示例 2：
输入：nums = [1]
输出：[1]
示例 3：
输入：[1,1,1,3,3,2,2,2]
输出：[1,2]
'''


# 空间复杂度不符合题目的要求
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1 = {}
        for each in nums:
            if each in dict1:
                dict1[each] += 1
            else:
                dict1[each] = 1
        count = len(nums) // 3
        res = []
        for key in dict1:
            if dict1[key] > count:
                res.append(key)
        return res
