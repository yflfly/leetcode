# coding:utf-8
'''
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


# 方法一：暴力方法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 方法二：哈希表法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
'''
方法一的时间复杂度较高的原因是寻找target-x的时间复杂度过高。
因此我们需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。如果存在，我们需要找出它的索引
使用哈希表，可以将寻找target-x的时间复杂度从O(N)降低到O(1)
我们创建一个哈希表，对于每一个x，我们首先查询到哈希表中是否存在target-x，然后将x插入到哈希表中，即可保证不会让x和自己匹配
'''


# 复现哈希表法 2021.1.28
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if target-nums[i] in dict1:
                return [dict1[target-nums[i]],i]
            dict1[nums[i]] = i
        return []