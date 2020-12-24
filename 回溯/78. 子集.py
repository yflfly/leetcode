# coding:utf-8
'''
78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

# 回溯方法(递归)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        res = []
        n = len(nums)
        helper(0, [])
        return res
# 迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

'''
代码讲解网址：
https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
'''
