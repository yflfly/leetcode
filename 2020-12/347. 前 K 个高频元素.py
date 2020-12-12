# coding:utf-8
'''
347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:
输入: nums = [1], k = 1
输出: [1]
 
提示：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dict1 = {}
        for each in nums:
            if each in dict1:
                dict1[each] += 1
            else:
                dict1[each] = 1
        list1 = sorted(dict1.items(), key=lambda kv: (kv[1], kv[0]))
        tag = 0
        for each in list1[::-1]:
            tag += 1
            if tag <= k:
                res.append(each[0])
        return res
