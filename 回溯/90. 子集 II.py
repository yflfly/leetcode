# coding:utf-8
'''
90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, path):
            if path not in res:
                res.append(path)
            for j in range(i, len(nums)):
                backtrack(j + 1, path + [nums[j]])

        if not nums:
            return []
        nums.sort()  # 进行了一个排序
        res = []
        backtrack(0, [])
        return res
